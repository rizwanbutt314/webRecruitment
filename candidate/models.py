import django
from django.utils.timezone import datetime
from django.core.exceptions import ValidationError
from django.db import models


# Create your models here.
class Candidate(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    resume = models.FileField(upload_to='uploads/')


class Technology(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField('Description')


class Current_Opening(models.Model):
    tech_id = models.ForeignKey(Technology, on_delete=models.CASCADE)
    experience = models.CharField(max_length=20)
    desc = models.CharField(max_length=500)
    opening_date = models.DateTimeField(default = django.utils.timezone.now, blank=True, null=True)
    closing_date = models.DateTimeField(default = django.utils.timezone.now, blank=True, null=True)