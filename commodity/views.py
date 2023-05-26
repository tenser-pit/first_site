from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.views.generic import ListView, TemplateView

from .models import *


class ProdHome(ListView):
    model = Category
    context_object_name = 'cats'
    template_name = 'commodity/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return Category.objects.order_by('name')


class ProdCategory(ListView):
    model = Commodity
    context_object_name = 'goods'
    template_name = 'commodity/category.html'

    # paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        current_category = Category.objects.get(slug=self.kwargs['cat_slug']).name
        context = super().get_context_data(**kwargs)
        context['category'] = current_category
        context['title'] = 'Категория' + current_category
        context['cat_slug'] = self.kwargs['cat_slug']

        return context

    def get_queryset(self):
        return Commodity.objects.filter(cat=Category.objects.get(slug=self.kwargs['cat_slug']).id)


class ProdGoods(ListView):
    model = Commodity
    context_object_name = 'goods'
    template_name = 'commodity/goods.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        current_goods = Commodity.objects.get(slug=self.kwargs['goods_slug']).name
        context['title'] = 'Товар' + current_goods
        context['goods_slug'] = self.kwargs['goods_slug']

        return context

    def get_queryset(self):
        return Commodity.objects.filter(slug=self.kwargs['goods_slug'])


class ProdCart(LoginRequiredMixin, TemplateView):
    template_name = 'commodity/cart.html'
    raise_exception = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Корзина товаров'

        return context


def about(request):
    return render(request, 'commodity/about.html')


def contact(request):
    return render(request, 'commodity/contact.html')


def page_not_found(request, exception):
    return HttpResponseNotFound(request, 'commodity/404.html', status=404)
