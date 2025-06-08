from apps.core import models
from django.contrib import admin

[% for model in cookiecutter.models.split(' ') -%]
admin.site.register(models.[[ model ]])
[% endfor %]
