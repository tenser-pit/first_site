from django.db import models
from django.urls import reverse


class Commodity(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена')
    image = models.ImageField(upload_to='static/media/%Y/%m/%d/', verbose_name='Фото товара', blank=True)

    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('goods', kwargs={'goods_slug': self.slug})

    class Meta:
        verbose_name = 'Все товары'
        verbose_name_plural = 'Все товары'
        ordering = ['title', 'price']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    image = models.ImageField(upload_to='static/media/%Y/%m/%d/',)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Все категории'
        ordering = ['id']
