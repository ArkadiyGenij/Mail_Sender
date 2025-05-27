from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import RegisterForm, AuthForm


# Create your views here.
class RegisterView(CreateView):
    form_class = RegisterForm
    reverse_url = reverse_lazy('users:login')


class AuthView(LoginView):
    form_class = AuthForm
