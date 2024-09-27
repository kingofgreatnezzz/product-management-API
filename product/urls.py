from django.urls import path
from .views import SellProductAPIView

urlpatterns = [
    path('sell/', SellProductAPIView.as_view(), name='sell-product'),
]
