from django.urls import path
from django.views.generic import TemplateView
from apps.core import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    [% for model in cookiecutter.models.split(' ') -%]
    path('[[ model | kebab_case ]]/', views.[[ model ]]ListView.as_view()),
    path('[[ model | kebab_case ]]/new/', views.[[ model ]]CreateView.as_view()),
    path('[[ model | kebab_case ]]/<int:pk>/', views.[[ model ]]UpdateView.as_view()),
    path('[[ model | kebab_case ]]/<int:pk>/delete/', views.[[ model ]]DeleteView.as_view()),
    [% endfor -%]
]
