from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularRedocView, SpectacularAPIView
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('oauth/', include('apps.oauth.urls')),
    path('api/', include('apps.core.urls')),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/redoc/',
         SpectacularRedocView.as_view(url_name='schema'), name='redoc'
         ),
    path('', RedirectView.as_view(url='/api/schema/redoc/')),
]
