from django.urls import path
from .views import *

urlpatterns = [
  path('', get_all_products, name='products'),
  path('<int:id>', get_product, name='product'),
  path('create', create_product, name='create_product'),
  path('api', get_all_products_json, name='products_json')
]