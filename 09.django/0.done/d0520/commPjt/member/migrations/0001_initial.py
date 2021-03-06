# Generated by Django 4.0.4 on 2022-05-20 03:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('pw', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('nickname', models.CharField(max_length=100)),
                ('tel', models.CharField(max_length=13)),
                ('zipcode', models.CharField(max_length=6)),
                ('adress1', models.CharField(max_length=300)),
                ('adress2', models.CharField(max_length=300)),
                ('gender', models.CharField(max_length=7)),
                ('hobby', models.CharField(max_length=100)),
                ('createdate', models.DateTimeField(blank=True, verbose_name=datetime.datetime(2022, 5, 20, 12, 15, 1, 38511))),
                ('updatedate', models.DateTimeField(blank=True, verbose_name=datetime.datetime(2022, 5, 20, 12, 15, 1, 38511))),
            ],
        ),
    ]
