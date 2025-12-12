from django.core.management.base import BaseCommand
from django.db import transaction, IntegrityError
import threading
import time
from demoapp.models import TestModel, RelatedModel

class Command(BaseCommand):
    help = "Run experiments demonstrating Django signal properties."

    def handle(self, *args, **options):
        print("\n=== Experiment 1: Synchronous behaviour (order & blocking) ===")
        # Clean up
        TestModel.objects.all().delete()
        RelatedModel.objects.all().delete()

        start = time.time()
        print("[sender] creating TestModel (this will trigger receivers that sleep)")
        obj = TestModel.objects.create(name="sync-test")
        print("[sender] create returned, time elapsed:", time.time() - start)
        print("=> If receivers are synchronous, the sender.create printed only after receiver finished.")

        print("\n=== Experiment 2: Thread identity ===")
        TestModel.objects.all().delete()
        RelatedModel.objects.all().delete()
        main_thread_id = threading.get_ident()
        print("[sender] main thread id is:", main_thread_id)
        obj = TestModel.objects.create(name="thread-test")
        print("[sender] after create in thread id:", threading.get_ident())
        print("=> Observe printed thread ids from receivers above; they should match sender thread id.")

        print("\n=== Experiment 3: Transaction behaviour ===")
        TestModel.objects.all().delete()
        RelatedModel.objects.all().delete()
        try:
            with transaction.atomic():
                print("[sender] inside transaction.atomic: creating TestModel")
                obj = TestModel.objects.create(name="txn-test")
                # At this point post_save runs and our receiver creates RelatedModel.
                print("[sender] raising exception to force rollback")
                raise RuntimeError("force rollback")
        except RuntimeError:
            pass

        # After rollback, check DB for objects
        tm_exists = TestModel.objects.filter(name="txn-test").exists()
        rm_exists = RelatedModel.objects.filter(origin__startswith="from_signal_").exists()
        print(f"[sender] after rollback: TestModel exists? {tm_exists}")
        print(f"[sender] after rollback: RelatedModel created by signal exists? {rm_exists}")
        print("=> If both are False, the signal's DB writes were part of the same transaction and rolled back.")
