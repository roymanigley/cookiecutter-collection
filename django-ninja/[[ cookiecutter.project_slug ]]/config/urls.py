from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('oauth/', include('apps.oauth.urls')),
    path('api/', include('apps.core.urls')),
    path('', RedirectView.as_view(url='/api/docs')),
]
