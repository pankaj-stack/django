from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Category_model(models.Model):
    category =models.CharField(max_length=100)
    
class ProductModel(models.Model):
    product_name = models.CharField(max_length=1100)
    product_model_name = models.CharField(max_length=1100)
    price = models.IntegerField()
    product_category = models.CharField(max_length=100)