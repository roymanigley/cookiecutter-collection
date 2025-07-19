from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django import forms


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'nes-input'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'nes-input'}))

class CustomLoginView(LoginView):
    template_name = 'auth/login.html'
    form_class = CustomAuthenticationForm