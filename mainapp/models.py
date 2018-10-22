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
    analyst = models.OneToOneField(User, on_delete=models.CASCADE)
    analyte = models.CharField(max_length=100)
    instructions = models.TextField()
    
class SampleAnalysis (models.Model):
    lab_protocol = models.ForeignKey(LabProtocol, on_delete=models.CASCADE)
    requested_by = models.OneToOneField(User, on_delete=models.CASCADE)
    
    SAMPLE_ANALYSIS_STATUS = (
        ('REQ', 'Requested'),
        ('INP', 'In progress'),
        ('REJ', 'Rejected'),
        ('ONH', 'On hold'),
        ('APP', 'Approved'),
    )
    status = models.CharField(max_length=3, choices=SAMPLE_ANALYSIS_STATUS, default='')

class Instruments(models.Model):
    name = models.CharField(max_length=100)
    serial_no = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    calibration_freq_months = models.IntegerField()
    last_calibration_date = models.DateTimeField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    used_in = models.ManyToManyField(LabProtocol)

class Reagents(models.Model):
    name = models.CharField(max_length=100)
    lot_no = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    expiry_date = models.DateTimeField()
    used_in = models.ManyToManyField(LabProtocol)
    
    