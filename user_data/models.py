from django.contrib.auth.models import AbstractUser
from django.db import models


class UserData(AbstractUser):
    image = models.ImageField(upload_to='users', null=True, blank=True)
    is_author = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователи'
        ordering = ['username']
        indexes = [models.Index(fields=['username'])]
