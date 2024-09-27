from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    unit = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    
class ProductBatch(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="batches")
    quantity = models.IntegerField(default=0)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.product.name} Batch - {self.quantity} units"
    

class Sale(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    total_profit = models.DecimalField(max_digits=10, decimal_places=2)

class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    unit  = models.CharField(max_length=50)
    quantity = models.IntegerField(default=0)
    profit = models.DecimalField(max_digits=10, decimal_places=2)

