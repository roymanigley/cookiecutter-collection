from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.authentication.models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(UserAdmin):
    pass