from django.contrib.auth.models import AbstractUser
from django.db import models


class UserData(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    image = models.ImageField(upload_to='users', null=True, blank=True)
    is_author = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователи'
        ordering = ['username']
        indexes = [models.Index(fields=['username'])]
