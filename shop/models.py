from distutils.command.upload import upload
from itertools import product
from pyexpat import model
from django.db import models
from traitlets import default

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=50)
    category=models.CharField(max_length=50,default='')
    subcategory=models.CharField(max_length=50,default='')
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=50,default='')
    pub_date=models.DateField()
    image=models.ImageField(upload_to="images",default='')

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=70,default='')
    phone=models.CharField(max_length=70,default='')
    desc=models.CharField(max_length=500,default='')
    
    def __str__(self):
        return self.name



