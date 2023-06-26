from django.urls import path

from .views import *

app_name = 'cart'

urlpatterns = [
    path('', cart_detail, name='cart'),
    path('add/<int:product_id>/', add_cart, name='add_cart'),
    path('decrease/<int:product_id>/', decrement_cart, name='decrease_cart'),
    path('remove/<int:product_id>', remove_cart, name='remove_cart'),
]