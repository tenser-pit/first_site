from django.db import models
from django.urls import reverse

from user_data.models import UserData
from ProductSite import settings


class Category(models.Model):
    name = models.CharField(unique=True, max_length=100, db_index=True, verbose_name='Категория')
    image = models.ImageField(null=True, blank=True, upload_to='category',)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Все категории'
        ordering = ['name']
        indexes = [models.Index(fields=['name'])]


class Commodity(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(null=True, upload_to='commodity', verbose_name='Фото товара', blank=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('goods', kwargs={'goods_slug': self.slug})

    class Meta:
        verbose_name = 'Все товары'
        verbose_name_plural = 'Все товары'
        ordering = ['name', 'price']
        indexes = [models.Index(fields=['name'])]


class Bucket(models.Model):
    quantity = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    product = models.ForeignKey('Commodity', on_delete=models.PROTECT)

    class Meta:
        verbose_name = ''
        verbose_name_plural = ''
        ordering = ['product', 'user']