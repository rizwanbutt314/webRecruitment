# Generated by Django 2.0.6 on 2018-10-17 10:50

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('resume', models.FileField(upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='Current_Opening',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience', models.CharField(max_length=20)),
                ('desc', models.CharField(max_length=500)),
                ('opening_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('closing_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('desc', models.TextField(verbose_name='Description')),
            ],
        ),
        migrations.AddField(
            model_name='current_opening',
            name='tech_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidate.Technology'),
        ),
    ]