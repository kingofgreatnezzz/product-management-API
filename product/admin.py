from django.contrib import admin
from .models import Product, Sale

# Registering Product with search functionality for name and filtering by date
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'quantity', 'selling_price', 'cost_price', 'category' )
    search_fields = ('product_name',)  # Allows searching by product name
    list_filter = ['category'] # Allows filtering by date and category

# Registering Sale with search and filter functionality
@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity_sold', 'total_price', 'profit', 'sale_date')
    search_fields = ('product',)  # Allows searching sales by product name
    list_filter = ['sale_date']  # Allows filtering sales by date
