from django.db import models


class Product(models.Model):
    
    p_no  = models.AutoField(primary_key=True)
    p_name = models.CharField(max_length=100)
    p_servings  = models.CharField(max_length=100)
    p_unitPrice = models.IntegerField(max_length=10, default=0)
    p_description = models.TextField()
    p_category =models.CharField(max_length=20,default='요리')
    p_manufacturer  = models.CharField(max_length=20,blank=True)
    p_unit  = models.IntegerField(max_length=20,default=100)
    p_fileName =models.ImageField(max_length=100,blank=True)
    

    def __str__(self):
        return self.p_name