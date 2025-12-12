# demoapp/models.py
from django.db import models

class TestModel(models.Model):
    name = models.CharField(max_length=100)

class RelatedModel(models.Model):
    origin = models.CharField(max_length=100)
    created_by_signal = models.BooleanField(default=False)
