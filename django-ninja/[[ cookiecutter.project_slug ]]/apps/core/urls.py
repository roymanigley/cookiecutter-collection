from django.urls import path
from apps.core.api import ninja_api

urlpatterns = [
    path('', ninja_api.urls),
]
