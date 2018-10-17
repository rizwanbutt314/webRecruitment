import django
from django.utils.timezone import datetime
from django.core.exceptions import ValidationError
from django.db import models



class Technology(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField('Description')


class Current_Opening(models.Model):
    tech_id = models.ForeignKey(Technology, on_delete=models.CASCADE)
    experience = models.FloatField(max_length=3)
    desc = models.CharField(max_length=500)
    opening_date = models.DateTimeField(default=django.utils.timezone.now, blank=True, null=True)
    closing_date = models.DateTimeField(default=django.utils.timezone.now, blank=True, null=True)


class Recruitment_User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    is_admin = models.BooleanField()
    is_hr = models.BooleanField()
    is_interviewer = models.BooleanField()
    is_manager = models.BooleanField()


class Tech_Opening(models.Model):
    tech_id = models.ForeignKey(Technology, on_delete=models.DO_NOTHING)
    opening_id = models.ForeignKey(Current_Opening, on_delete=models.DO_NOTHING)

# Create your models here.
class Candidate(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    resume = models.FileField(upload_to='uploads/')
    reference_id = models.ForeignKey(Recruitment_User,null=True, on_delete=models.DO_NOTHING)


