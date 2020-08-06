from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from .forms import RegistrationForm, LoginForm
from django.views.generic import CreateView, DetailView
from .models import BlogUser


# Create your views here.
class UserLoginView(LoginView):
    template_name = 'usersapp/login.html'
    form_class = LoginForm


class UserCreateView(CreateView):
    model = BlogUser
    template_name = 'usersapp/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('users:login')


class UserDetailView(DetailView):
    model = BlogUser
    template_name = 'usersapp/profile.html'
