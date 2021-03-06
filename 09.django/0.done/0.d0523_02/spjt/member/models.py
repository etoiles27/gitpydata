from django.db import models
from datetime import datetime


class Member(models.Model):
    id = models.CharField(max_length=30, primary_key=True)
    pw = models.CharField(max_length=300)
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    tel = models.CharField(max_length=13, blank=True)
    zipcode = models.CharField(max_length=6, blank=True)
    adress1 = models.CharField(max_length=300, blank=True)
    adress2 = models.CharField(max_length=300, blank=True)
    gender = models.CharField(max_length=7, default='남자')
    hobby = models.CharField(max_length=100, blank=True)
    createdate = models.DateTimeField(datetime.now(), blank=True)
    updatedate = models.DateTimeField(datetime.now(), blank=True)
    
    
    def __str__(self):
        return self.id