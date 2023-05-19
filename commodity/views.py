from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView

from .forms import *
from .utils import *
from .models import *


class THome(DataMixin, ListView):
    model = Category
    context_object_name = 'cats'
    template_name = 'commodity/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Category.objects.order_by('name')


class TCategory(DataMixin, ListView):
    model = Commodity
    context_object_name = 'goods'
    template_name = 'commodity/category.html'
    # paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        current_category = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(title='Категория:' + current_category.name,
                                      category=current_category.name,
                                      cat_slug=self.kwargs['cat_slug'],
                                      )
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Commodity.objects.filter(cat=Category.objects.get(slug=self.kwargs['cat_slug']).id)


class TGoods(DataMixin, ListView):
    model = Commodity
    context_object_name = 'goods'
    template_name = 'commodity/goods.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Товар:' + Commodity.objects.get(slug=self.kwargs['goods_slug']).name,
                                      goods_slug=self.kwargs['goods_slug'])
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Commodity.objects.filter(slug=self.kwargs['goods_slug'])


class TLogin(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'commodity/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Вход')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


class TRegister(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'commodity/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class TCart(LoginRequiredMixin, DataMixin, TemplateView):
    template_name = 'commodity/cart.html'
    raise_exception = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Корзина')
        return dict(list(context.items()) + list(c_def.items()))


class TProfile(LoginRequiredMixin, DataMixin, TemplateView):
    template_name = 'commodity/profile.html'
    raise_exception = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Профиль пользователя')
        return dict(list(context.items()) + list(c_def.items()))


def logout(request):
    logout(request)
    return redirect('home')


def about(request):
    return render(request, 'commodity/about.html')


def contact(request):
    return render(request, 'commodity/contact.html')


def pageNotFound(request, exeption):
    return HttpResponseNotFound('<h1>This is error 404</h1>')
