from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from user_data.forms import LoginUserForm, RegisterUserForm, ProfileForm


class UserLogin(LoginView):
    form_class = LoginUserForm
    template_name = 'user_data/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Вход в личный кабинет'
        return context

    def get_success_url(self):
        return reverse_lazy('commodity:home')


class UserRegister(CreateView):
    form_class = RegisterUserForm
    template_name = 'user_data/register.html'
    success_url = reverse_lazy('user_data:login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('commodity:home')


class UserProfile(LoginRequiredMixin, TemplateView):
    model = ProfileForm
    template_name = 'user_data/profile.html'
    raise_exception = True

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.form = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Профиль пользователя'
        context['form'] = self.form
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            self.form = UserProfile(data=request.POST)
            if self.form.is_valid():
                self.form.save()
                return redirect('user')
            else:
                self.form = request.user
        return super(UserProfile, self).dispatch(request, *args, **kwargs)


def user_logout(request):
    logout(request)
    return redirect('commodity:home')

