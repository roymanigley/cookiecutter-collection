[%- for model in cookiecutter._models -%]
from apps.core.models import [[ model ]]
from django import forms
from django.utils.translation import gettext_lazy as _


class [[ model ]]Form(forms.ModelForm):

    name = forms.CharField(
        widget=forms.widgets.TextInput(
            {'class': 'input w-full', 'placeholder': _('Name')}
        )
    )

    class Meta:
        model = [[ model ]]
        fields = '__all__'
        table_display_fields = [
            'name', 
            'created_by', 
            'created_at', 
            'updated_by', 
            'updated_at'
        ]

### NEEDLE: apps/core/forms/[[ model | snake_case ]]_form.py
[% endfor -%]
