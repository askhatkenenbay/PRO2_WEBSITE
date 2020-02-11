# Generated by Django 3.0 on 2020-02-10 18:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20200130_1031'),
    ]

    operations = [
        migrations.CreateModel(
            name='SurveyStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('client_name', models.CharField(max_length=100)),
                ('goal', models.CharField(max_length=1000)),
                ('subject', models.CharField(max_length=500)),
                ('money', models.CharField(max_length=500)),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Date')),
            ],
        ),
    ]
