# Generated by Django 3.0 on 2020-01-30 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20200129_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theorylaw',
            name='more',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='theorylaw',
            name='text',
            field=models.TextField(),
        ),
    ]
