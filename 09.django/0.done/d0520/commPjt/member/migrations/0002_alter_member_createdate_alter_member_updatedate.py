# Generated by Django 4.0.4 on 2022-05-20 06:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='createdate',
            field=models.DateTimeField(blank=True, verbose_name=datetime.datetime(2022, 5, 20, 15, 50, 15, 960282)),
        ),
        migrations.AlterField(
            model_name='member',
            name='updatedate',
            field=models.DateTimeField(blank=True, verbose_name=datetime.datetime(2022, 5, 20, 15, 50, 15, 960282)),
        ),
    ]