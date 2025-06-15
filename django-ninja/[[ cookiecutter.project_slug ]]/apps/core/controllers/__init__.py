[%- for model in cookiecutter._models -%]
from apps.core.controllers.[[ model | snake_case ]]_controller import [[ model ]]Controller
[% endfor -%]