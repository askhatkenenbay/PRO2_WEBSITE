# Generated by Django 3.0 on 2020-01-30 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20200130_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='is_optional',
            field=models.BooleanField(),
        ),
    ]