[%- for model in cookiecutter._models -%]
from apps.core.forms.[[ model | snake_case ]]_form import [[ model ]]Form
[% endfor -%]
