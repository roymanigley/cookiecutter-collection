from django.urls import path, include, re_path
from apps.oauth import views

urlpatterns = [
    re_path(r"^applications/.*$", views.not_found_view),
    path('', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
