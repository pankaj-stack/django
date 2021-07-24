from django.contrib import admin
from .models import Category_model
from .models import ProductModel

# Register your models here.
@admin.register(ProductModel)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['product_name','product_model_name','price','product_category']



