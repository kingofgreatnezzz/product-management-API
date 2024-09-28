# product_mgmt/views.py

from rest_framework import generics
from .models import Product, ProductBatch, Sale
from .serializers import ProductSerializer, ProductBatchSerializer, SaleSerializer

# API for Product Creation
class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# API for Retrieving Product Information
class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# API for Adding Quantity to Products
class AddQuantityAPIView(generics.CreateAPIView):
    queryset = ProductBatch.objects.all()
    serializer_class = ProductBatchSerializer

# API for Selling Products
class SellProductAPIView(generics.CreateAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

    def perform_create(self, serializer):
        # Create and validate all the sales parameters
        product = serializer.validated_data['product']
        quantity_sold = serializer.validated_data['quantity_sold']
        unit_measurement = serializer.validated_data['unit_measurement']
        total_price = quantity_sold * product.selling_price

        # Calculate profit using FIFO (First In, First Out)
        batches = ProductBatch.objects.filter(product=product).order_by('added_at')
        # Quantity_left is amount of product to be bought
        quantity_left = quantity_sold
        cost_price_total = 0

        for batch in batches:
            if quantity_left == 0:
                break
                 
            # Calculates cost price for sold quantity
            if batch.quantity_added >= quantity_left:
                cost_price_total += quantity_left * batch.cost_price
                batch.quantity_added -= quantity_left
                batch.save()
                quantity_left = 0
            else:
                cost_price_total += batch.quantity_added * batch.cost_price
                quantity_left -= batch.quantity_added
                batch.quantity_added = 0
                batch.save()

        profit = total_price - cost_price_total

        serializer.save(total_price=total_price, profit=profit)
        product.quantity -= quantity_sold
        product.save()

# API for Retrieving Sales History
class SalesHistoryAPIView(generics.ListAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
