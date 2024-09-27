# product_mgmt/models.py

from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    unit_measurement = models.CharField(max_length=50)  # e.g., "KG", "Piece", etc.

    def __str__(self):
        return self.product_name

class ProductBatch(models.Model):
    product = models.ForeignKey(Product, related_name='batches', on_delete=models.CASCADE)
    quantity_added = models.IntegerField()
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    added_at = models.DateTimeField(auto_now_add=True)

class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_sold = models.IntegerField()
    unit_measurement = models.CharField(max_length=50)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    profit = models.DecimalField(max_digits=10, decimal_places=2)
    sale_date = models.DateTimeField(auto_now_add=True)
