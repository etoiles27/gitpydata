# Generated by Django 4.0.4 on 2022-05-20 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Freeboard',
            fields=[
                ('f_no', models.AutoField(primary_key=True, serialize=False)),
                ('id', models.CharField(max_length=100)),
                ('f_title', models.CharField(max_length=1000)),
                ('f_content', models.TextField()),
                ('f_group', models.IntegerField(default=0)),
                ('f_step', models.IntegerField(default=0)),
                ('f_indent', models.IntegerField(default=0)),
                ('f_hit', models.IntegerField(default=1)),
                ('f_createdate', models.DateTimeField(auto_now=True)),
                ('f_upedatedate', models.DateTimeField(auto_now=True)),
                ('f_file', models.ImageField(blank=True, upload_to='')),
            ],
        ),
    ]
