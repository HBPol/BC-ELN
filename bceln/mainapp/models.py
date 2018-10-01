from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Sample(models.Model):
    product = models.CharField(max_length=100)
    batch = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    storage_temp = models.CharField(max_length=100)


class LabProtocol(models.Model):
    sample = models.ForeignKey(Sample, on_delete=models.CASCADE)
    analyst = models.ForeignKey(User, on_delete=models.CASCADE)
    analyte = models.CharField(max_length=100)
    instructions = models.TextField()