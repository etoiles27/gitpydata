# Generated by Django 4.0.5 on 2022-06-17 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminPage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('c_No', models.AutoField(primary_key=True, serialize=False)),
                ('c_name', models.CharField(blank=True, max_length=100, null=True)),
                ('c_email', models.CharField(blank=True, max_length=1000, null=True)),
                ('c_tel', models.CharField(blank=True, max_length=13, null=True)),
                ('c_title', models.CharField(blank=True, max_length=1000, null=True)),
                ('c_content', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
