# Generated by Django 3.0 on 2019-12-19 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20191219_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='person',
            name='password',
            field=models.CharField(max_length=1000),
        ),
    ]
