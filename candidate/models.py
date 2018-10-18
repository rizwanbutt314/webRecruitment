import django
from django.utils.timezone import datetime
from django.db import models


class Technology(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField('Description')


class CurrentOpening(models.Model):
    experience = models.FloatField(max_length=3)
    desc = models.TextField('Opening Description')
    opening_timestamp = models.DateTimeField(default=django.utils.timezone.now, blank=True, null=True)
    closing_timestamp = models.DateTimeField(default=django.utils.timezone.now, blank=True, null=True)


class RecruitmentUser(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    is_admin = models.NullBooleanField()
    is_hr = models.NullBooleanField()
    is_interviewer = models.NullBooleanField()
    is_manager = models.NullBooleanField()


class TechnologyOpening(models.Model):
    tech_id = models.ForeignKey(Technology, on_delete=models.DO_NOTHING)
    opening_id = models.ForeignKey(CurrentOpening, on_delete=models.DO_NOTHING)


class Candidate(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    resume = models.FileField(upload_to='uploads/')
    reference_id = models.ForeignKey(RecruitmentUser, null=True, on_delete=models.DO_NOTHING)


class CandidateAppliedOpening(models.Model):
    candidate_id = models.ForeignKey(Candidate, null=True, on_delete=models.DO_NOTHING)
    current_opening_id = models.ForeignKey(CurrentOpening, null=True, on_delete=models.DO_NOTHING)
