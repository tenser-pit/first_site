from django.forms import model_to_dict
from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from django.views import View
from django.views.generic import ListView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *

# class ProdHomeApi(APIView):
#     def get(self, request):
#         lst = Products.objects.all().values()
#         return Response({'title': list(lst)})
#
#     def post(self, request):
#         return Response({'post': 'adaw'})
#

# TODO
# class ProdHomeApi(generics.ListAPIView):
#     queryset = Category.objects.all()
#     serializer_class = ProductSerializer


def product_main(request):
    return render(request, 'product/index.html')


class ProdMain(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'product/main.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Все категории'
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



def about(request):
    return render(request, 'product/about.html')


def contact(request):
    return render(request, 'product/contact.html')


def page_not_found(request, exception):
    return HttpResponseNotFound(request, 'product/404.html', status=404)
