from django.db import models
from datetime import datetime

# Create your models here.
class Member(models.Model):
    id = models.CharField(max_length=30, primary_key=True)
    pw = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    tel = models.CharField(max_length=13)
    zipcode = models.CharField(max_length=6)
    adress1 = models.CharField(max_length=300)
    adress2 = models.CharField(max_length=300)
    gender = models.CharField(max_length=7)
    hobby = models.CharField(max_length=100)
    createdate = models.DateTimeField(datetime.now(), blank=True)
    updatedate = models.DateTimeField(datetime.now(), blank=True)
    
    
    def __str__(self):
        return self.id