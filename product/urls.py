from django.urls import path

from product_mgmt.product import admin
from .views import SellProductAPIView

urlpatterns = [
     path('admin/', admin.site.urls),
    path('api/sell/', SellProductAPIView.as_view(), name='sell-product'),
]