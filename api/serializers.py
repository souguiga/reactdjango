from rest_framework import serializers
from api.models import Category, Product, Sale

# Serializers define the API representation.
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [ 'id', 'title' ]

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ['id', 'category', 'name', 'description', 'filename', 'price']

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ["id", "name", "address1", "address2", "city", "state", "zipcode", "total", "items", "payment_intent"]