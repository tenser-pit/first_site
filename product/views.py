from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from django.views.generic import ListView

from .models import *


class ProdHome(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'product/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return Category.objects.order_by('name')


class ProdCategory(ListView):
    model = Products
    context_object_name = 'products'
    template_name = 'product/category.html'

    # paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        current_category = Category.objects.get(slug=self.kwargs['cat_slug']).name
        context = super().get_context_data(**kwargs)
        context['category'] = current_category
        context['title'] = 'Категория' + current_category
        context['cat_slug'] = self.kwargs['cat_slug']

        return context

    def get_queryset(self):
        return Products.objects.filter(cat=Category.objects.get(slug=self.kwargs['cat_slug']).id)


class ProdGoods(ListView):
    model = Products
    context_object_name = 'products'
    template_name = 'product/products.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        current_product = Products.objects.get(slug=self.kwargs['goods_slug']).name
        context['title'] = 'Товар' + current_product
        context['goods_slug'] = self.kwargs['product_slug']
        return context

    def get_queryset(self):
        return Products.objects.filter(slug=self.kwargs['product_slug'])


class ProdCart(ListView):
    model = Cart
    context_object_name = 'cart'
    template_name = 'product/cart.html'
    raise_exception = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Корзина товаров'
        return context

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)


def add_cart(request, product_id):
    product = Products.objects.get(id=product_id)
    cart = Cart.objects.filter(user=request.user, product=product)

    if not cart.exists():
        Cart.objects.create(user=request.user, product=product, quantity=1)
    else:
        current_cart = cart.first()
        current_cart.quantity += 1
        current_cart.save()

    return redirect(request.META['HTTP_REFERER'])


def about(request):
    return render(request, 'product/about.html')


def contact(request):
    return render(request, 'product/contact.html')


def page_not_found(request, exception):
    return HttpResponseNotFound(request, 'product/404.html', status=404)
