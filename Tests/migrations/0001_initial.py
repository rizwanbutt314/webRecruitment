# Generated by Django 2.0.6 on 2018-10-17 07:44

import Tests.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Options',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('is_Answer', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testTime', models.TimeField(db_column='TestTime', default=10)),
                ('name', models.TextField(default='Singleton Test')),
                ('description', models.TextField(default='One Test for All.')),
                ('passingMarks', models.IntegerField(default='0')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Tests.Test'),
        ),
        migrations.AddField(
            model_name='options',
            name='question',
            field=models.ForeignKey(default=Tests.models.Options.question_default, on_delete=django.db.models.deletion.SET_DEFAULT, to='Tests.Question'),
        ),
    ]