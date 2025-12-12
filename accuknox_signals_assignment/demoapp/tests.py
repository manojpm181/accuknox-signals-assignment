# demoapp/tests.py
from django.test import TestCase
from django.db import transaction
from demoapp.models import TestModel, RelatedModel

class SignalTransactionTest(TestCase):
    def test_signal_runs_in_same_transaction(self):
        # Ensure DB is empty
        TestModel.objects.all().delete()
        RelatedModel.objects.all().delete()

        with self.assertRaises(RuntimeError):
            with transaction.atomic():
                obj = TestModel.objects.create(name="txn-test")
                raise RuntimeError("force rollback")

        self.assertFalse(TestModel.objects.filter(name="txn-test").exists())
        self.assertFalse(RelatedModel.objects.filter(origin__startswith="from_signal_").exists())
