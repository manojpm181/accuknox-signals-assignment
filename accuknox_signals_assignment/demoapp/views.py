from django.http import JsonResponse
from django.db import transaction
from .models import TestModel
from rectangle.rectangle import Rectangle



def test_view(request):
    return JsonResponse({"message": "Django is running successfully"})


def rectangle_view(request):
    r = Rectangle(5, 3)
    output = [item for item in r]
    return JsonResponse({"rectangle_output": output})


def signal_test_view(request):
    with transaction.atomic():
        obj = TestModel.objects.create(name="Signal Test Triggered")

    return JsonResponse({"status": "Signal Executed", "created_id": obj.id})
