# Generated by Django 4.0.4 on 2022-06-13 08:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Member', '0003_alter_members_createdate_alter_members_modidate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='createdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 6, 13, 8, 54, 51, 335523)),
        ),
        migrations.AlterField(
            model_name='members',
            name='modidate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 6, 13, 8, 54, 51, 335543)),
        ),
    ]