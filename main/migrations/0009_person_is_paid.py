# Generated by Django 3.0 on 2020-01-19 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20200119_0948'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
    ]