from django.db import models
from django.urls import reverse

# from user_data.models import UserData
from ProductSite import settings


class Category(models.Model):
    name = models.CharField(unique=True, max_length=100, db_index=True, verbose_name='Категория')
    image = models.ImageField(null=True, blank=True, upload_to='category',)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product:category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Все категории'
        ordering = ['name']
        indexes = [models.Index(fields=['name'])]


class Products(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(null=True, upload_to='product', verbose_name='Фото товара', blank=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def __str__(self):
            return self.name

    def get_absolute_url(self):
        return reverse('product:product', kwargs={'product_slug': self.slug})

    class Meta:
        verbose_name = 'Все товары'
        verbose_name_plural = 'Все товары'
        ordering = ['name', 'price']
        indexes = [models.Index(fields=['name'])]

