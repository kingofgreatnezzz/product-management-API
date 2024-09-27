from rest_framework import serializers
from .models import *

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'unit', 'selling_price']

class ProductBatchSerializers(serializers.ModelSerializers):
    class Meta:
        model = ProductBatch
        fields = ['id', 'product', 'cost_price', 'date_added']

class SaleItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleItem
        fields = ['product', 'unit' ,'quantity', 'profit']

class SaleSerializer(serializers.ModelSerializer):
    items = SaleItemSerializer(many=True)
    class Meta:
        model = Sale
        fields = ['id', 'total_profit', 'items']
        
