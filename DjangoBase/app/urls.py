from django.urls import path
from django.urls.conf import include
from .views import ProductList, SearchCoordsView

urlpatterns = [
    path('valerdat/products/', ProductList.as_view(), name='products-list'),
    path('valerdat/searchcoords/', SearchCoordsView.as_view(), name='search-products'),
]