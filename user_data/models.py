from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    image = models.ImageField(upload_to='users', null=True, blank=True)
