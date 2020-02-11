# Generated by Django 3.0 on 2020-02-10 18:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_surveystudent_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='SurveyTutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(default='empty', max_length=250)),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('money', models.CharField(max_length=500)),
                ('rec', models.CharField(max_length=500)),
            ],
        ),
    ]
