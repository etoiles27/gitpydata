# Generated by Django 4.0.4 on 2022-05-18 03:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students', '0002_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('s_no', models.AutoField(primary_key=True, serialize=False)),
                ('s_name', models.CharField(max_length=100)),
                ('s_major', models.CharField(max_length=100)),
                ('s_age', models.IntegerField(default=0)),
                ('s_grade', models.IntegerField(default=0)),
                ('s_gender', models.CharField(max_length=30)),
                ('s_hobby', models.CharField(max_length=100)),
                ('s_date', models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 18, 12, 8, 22, 520978))),
            ],
        ),
    ]
