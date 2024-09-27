from django.urls import path
from .views import *

urlpatterns = [
    path('create/', ProductCreateAPIView.as_view(), name='product-create'),
    path('products/', ProductListAPIView.as_view(), name='product-list'),
    path('add-quantity/', AddQuantityAPIView.as_view(), name='add-quantity'),
    path('sell/', SellProductAPIView.as_view(), name='sell-product'),
    path('sales-history/', SalesHistoryAPIView.as_view(), name='sales-history'),
]
