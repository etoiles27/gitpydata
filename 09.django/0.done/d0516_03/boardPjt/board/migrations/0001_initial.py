# Generated by Django 4.0.4 on 2022-05-16 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bno', models.IntegerField(default=0)),
                ('uid', models.CharField(max_length=20)),
                ('btitle', models.CharField(max_length=200)),
                ('bcontent', models.CharField(max_length=3000)),
                ('bdate', models.DateField(auto_now=True)),
                ('bgroup', models.IntegerField(default=0)),
                ('bstep', models.IntegerField(default=0)),
                ('bindent', models.IntegerField(default=0)),
                ('bhit', models.IntegerField(default=0)),
                ('bimg', models.CharField(max_length=200)),
            ],
        ),
    ]
