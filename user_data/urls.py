from django.urls import path
from user_data.views import *

app_name = 'user_data'

urlpatterns = [
    path('profile/', ProdProfile.as_view(), name='profile'),
    path('login/', ProdLogin.as_view(), name='login'),
    path('logout/', logout, name='logout'),
    path('register/', ProdRegister.as_view(), name='register'),
]
