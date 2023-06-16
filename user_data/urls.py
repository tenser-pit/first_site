from django.urls import path
from user_data.views import *

app_name = 'user_data'

urlpatterns = [
    path('profile/', UserProfile.as_view(), name='profile'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', UserRegister.as_view(), name='register'),
]
