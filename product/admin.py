from django.contrib import admin

from .models import *

# Декоратор admin.register замена admin.site.register()


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'image',)
    list_display_links = ('name',)
    search_fields = ('name', 'content')
    list_filter = ('price',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
