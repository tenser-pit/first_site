from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from user_data.forms import LoginUserForm, RegisterUserForm


class ProdLogin(LoginView):
    form_class = LoginUserForm
    template_name = 'user_data/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Вход в личный кабинет'
        return context

    def get_success_url(self):
        return reverse_lazy('home')


class ProdRegister(CreateView):
    form_class = RegisterUserForm
    template_name = 'user_data/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class ProdProfile(LoginRequiredMixin, TemplateView):
    template_name = 'user_data/profile.html'
    raise_exception = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Профиль пользователя'

        return context


def logout(request):
    logout(request)
    return redirect('home')

