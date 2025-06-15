from apps.core import models
from django.contrib import admin


[% for model, model_values in cookiecutter._models.items() -%]
class [[ model ]]AdminModel(admin.ModelAdmin):
    search_fields = ("id", "[[ model_values.fields|first ]]",)
    list_display = ("id", "[[ model_values.fields|first ]]")
[% endfor %]

[% for model in cookiecutter._models -%]
admin.site.register(models.[[ model ]], [[ model ]]AdminModel)
[% endfor %]
