[%- for model, model_values in cookiecutter._models.items() -%]
from apps.core import models
from apps.shared import widgets
from django import forms


class [[ model ]]Form(forms.ModelForm):
    [% for field, field_values in model_values.fields.items() -%]
    [[field | as_form_field(field_values, model)]]
    [% endfor -%]

    class Meta:
        model = models.[[ model ]]
        fields = [
            [% for field, field_values in model_values.fields.items() -%]
            '[[ field ]]',
        [% endfor -%]
        ]

### NEEDLE: apps/core/forms/[[ model | snake_case ]]_form.py
[% endfor -%]
