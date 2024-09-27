from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product, ProductBatch, Sale, SaleItem
from .serializers import SaleSerializer

class SellProductAPIView(APIView):

    def post(self, request):
        sale_data = request.data.get('sale')
        total_profit = 0
        sale_items = []
        
        # Loop over products being sold
        for item in sale_data['items']:
            product = Product.objects.get(id=item['product_id'])
            quantity_to_sell = item['quantity']
            unit = item['unit']
            selling_price = product.selling_price
            
            # Track how much we've sold from each batch
            remaining_quantity = quantity_to_sell
            batch_profits = 0

            # Get batches of product (FIFO: oldest first)
            batches = ProductBatch.objects.filter(product=product).order_by('date_added')
            
            for batch in batches:
                if remaining_quantity <= 0:
                    break  # Stop if we've sold everything

                # How much can we sell from this batch?
                sell_from_batch = min(batch.quantity, remaining_quantity)

                # Calculate profit for this batch
                profit_per_unit = selling_price - batch.cost_price
                batch_profit = profit_per_unit * sell_from_batch
                batch_profits += batch_profit
                
                # Deduct the sold quantity from the batch
                batch.quantity -= sell_from_batch
                batch.save()

                # Deduct from remaining quantity to sell
                remaining_quantity -= sell_from_batch

            # Record the item in the sale
            sale_item = SaleItem(
                product=product,
                unit=unit,
                quantity=quantity_to_sell,
                profit=batch_profits
            )
            sale_items.append(sale_item)
            total_profit += batch_profits

        # Create a new Sale record
        sale = Sale.objects.create(total_profit=total_profit)
        for sale_item in sale_items:
            sale_item.sale = sale
            sale_item.save()

        serializer = SaleSerializer(sale)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
