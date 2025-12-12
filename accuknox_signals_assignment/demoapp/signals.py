# demoapp/signals.py
import threading
import time
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import TestModel, RelatedModel

# Receiver A: demonstrate synchronous behaviour via sleep/order printing
@receiver(post_save, sender=TestModel)
def receiver_sync_order(sender, instance, created, **kwargs):
    # This receiver sleeps briefly and prints before returning.
    print("[receiver_sync_order] start - will sleep 1s")
    time.sleep(1)
    print("[receiver_sync_order] finished sleeping - instance id:", instance.pk)

# Receiver B: demonstrate same-thread behaviour
@receiver(post_save, sender=TestModel)
def receiver_thread_id(sender, instance, created, **kwargs):
    caller_thread = threading.get_ident()
    # print thread id (the sender will also print thread id; we compare)
    print(f"[receiver_thread_id] running in thread id: {caller_thread}")

# Receiver C: demonstrate DB transaction behaviour by creating RelatedModel in signal
@receiver(post_save, sender=TestModel)
def receiver_create_related(sender, instance, created, **kwargs):
    if created:
        print("[receiver_create_related] creating RelatedModel inside signal")
        RelatedModel.objects.create(origin=f"from_signal_{instance.pk}", created_by_signal=True)
        print("[receiver_create_related] RelatedModel created (but may be rolled back if txn rolls back)")
