# product_mgmt/serializers.py

from rest_framework import serializers
from .models import Product, ProductBatch, Sale

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'product_name', 'quantity', 'selling_price', 'cost_price', 'category', 'unit_measurement']

class ProductBatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductBatch
        fields = ['id', 'product', 'quantity_added', 'cost_price', 'added_at']

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ['id', 'product', 'quantity_sold', 'unit_measurement', 'total_price', 'profit', 'sale_date']
