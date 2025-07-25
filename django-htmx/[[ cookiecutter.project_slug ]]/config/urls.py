from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('apps.authentication.urls')),
    path('', include('apps.core.urls')),
    path('', TemplateView.as_view(template_name='index.html'))
]
