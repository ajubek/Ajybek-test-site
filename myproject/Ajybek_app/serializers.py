from .models import Category,Product
from  rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','category_name','category_image']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields =['id', 'product_name', 'price','owner',
                 'phone_number', 'product_image',
                   'description', 'created_date', 'product_type']