# Generated by Django 4.0.4 on 2022-05-24 02:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fboard', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fboard',
            name='f_createdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 24, 11, 26, 42, 27348)),
        ),
        migrations.AlterField(
            model_name='fboard',
            name='f_upedatedate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 24, 11, 26, 42, 27348)),
        ),
    ]
