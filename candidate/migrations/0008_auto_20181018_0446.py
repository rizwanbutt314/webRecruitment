# Generated by Django 2.0.6 on 2018-10-18 04:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0007_candidate_reference_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='current_opening',
            name='tech_id',
        ),
        migrations.RemoveField(
            model_name='recruitment_user',
            name='is_manager',
        ),
    ]