from django.contrib import admin
from .models import OrderProduct


@admin.register(OrderProduct)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'paid', 'quantity',]
    list_filter = ['user', 'paid']

