from django import forms
from django.contrib.auth import views
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):

    username = forms.CharField(
        widget=forms.widgets.TextInput({'class': 'input w-full'})
    )
    password = forms.CharField(
        widget=forms.widgets.PasswordInput({'class': 'input w-full'})
    )


class LoginView(views.LoginView):
    template_name = 'login.html'
    form_class = LoginForm

    def get_success_url(self):
        return '/'


class LogoutView(views.LogoutView):
    template_name = 'index.html'
