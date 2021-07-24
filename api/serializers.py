# from .models import Category_model
# from .models import ProductModel
from rest_framework import serializers



class Category_modelSerializer(serializers.Serializer):
    category =serializers.CharField(max_length=100)
    
class ProductModelSerializer(serializers.Serializer):
    product_name = serializers.CharField(max_length=1100)
    product_model_name = serializers.CharField(max_length=1100)
    price = serializers.IntegerField()
    product_category = serializers.CharField(max_length=100)