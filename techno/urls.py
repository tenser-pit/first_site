from django.urls import path
from .views import *

urlpatterns = [
    path('', THome.as_view(), name='home'),
    path('category/<slug:cat_slug>', TCategory.as_view(), name='category'),
    path('goods/<slug:goods_slug>', TGoods.as_view(), name='goods'),
    path('cart/', TCart.as_view(), name='cart'),
    path('profile/', TProfile.as_view(), name='profile'),
    path('login/', TLogin.as_view(), name='login'),
    path('logout/', logout, name='logout'),
    path('register/', TRegister.as_view(), name='register'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),


]

