# Generated by Django 3.0 on 2020-02-10 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_surveytutor'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='surveystudent',
            options={'get_latest_by': 'date'},
        ),
        migrations.AlterModelOptions(
            name='surveytutor',
            options={'get_latest_by': 'date'},
        ),
    ]