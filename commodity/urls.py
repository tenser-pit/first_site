from django.urls import path
from django.conf.urls import handler404

from .views import *

app_name = 'commodity'

urlpatterns = [
    path('', ProdHome.as_view(), name='home'),
    path('category/<slug:cat_slug>', ProdCategory.as_view(), name='category'),
    path('goods/<slug:goods_slug>', ProdGoods.as_view(), name='goods'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('cart/', ProdCart.as_view(), name='cart'),

]

handler404 = 'commodity.views.page_not_found'
