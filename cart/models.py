from django.db import models

from django.conf import settings
from product.models import Products


class OrderProduct(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.PROTECT)
    paid = models.BooleanField(default=False)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = 'Заказы'
        verbose_name_plural = 'Заказы'
