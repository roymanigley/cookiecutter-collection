from django.urls import path

from django.contrib.auth import views as auth_views
from apps.authentication import views

urlpatterns = [
    path('login/', views.CustomLoginView.as_view()),
    path('logout/', auth_views.LogoutView.as_view()),
]
