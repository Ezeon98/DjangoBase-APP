from django.urls import path
from django.urls.conf import include
from .views import ProductList

urlpatterns = [
    path('valerdat/products/', ProductList.as_view(), name='products-list'),
]