[%- for model in cookiecutter.models.split(' ') -%]
from apps.core.forms.[[ model | snake_case ]]_form import [[ model ]]Form
[% endfor -%]
