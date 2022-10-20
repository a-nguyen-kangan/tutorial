from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Car(models.Model):
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
