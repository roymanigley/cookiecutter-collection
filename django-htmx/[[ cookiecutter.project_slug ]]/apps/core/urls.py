from django.urls import path

from apps.core import views

urlpatterns = [
    [% for model in cookiecutter._models -%]
    path('[[ model | kebab_case ]]/', views.[[ model ]]ListView.as_view()),
    path('[[ model | kebab_case ]]/new/', views.[[ model ]]CreateView.as_view()),
    path('[[ model | kebab_case ]]/<int:pk>/edit/', views.[[ model ]]UpdateView.as_view()),
    path('[[ model | kebab_case ]]/<int:pk>/delete/', views.[[ model ]]DeleteView.as_view()),
    path('[[ model | kebab_case ]]/<int:pk>/', views.[[ model ]]DetailView.as_view()),
[% endfor -%]
]
