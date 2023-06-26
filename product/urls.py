from django.urls import path
from django.conf.urls import handler404

from .views import *

app_name = 'product'

urlpatterns = [
    path('', ProdHome.as_view(), name='home'),
    path('category/<slug:cat_slug>', ProdCategory.as_view(), name='category'),
    path('product/<slug:product_slug>', ProdGoods.as_view(), name='product'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),


]

handler404 = 'product.views.page_not_found'
