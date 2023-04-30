from django.contrib import admin

from .models import *


class TechnoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'photo',)
    list_display_links = ('title',)
    search_fields = ('title', 'content')
    list_filter = ('time_create', 'price',)
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Techno, TechnoAdmin)
admin.site.register(Category, CategoryAdmin)
