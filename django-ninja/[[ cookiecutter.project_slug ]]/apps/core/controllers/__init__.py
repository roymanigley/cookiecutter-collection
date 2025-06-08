[%- for model in cookiecutter.models.split(' ') -%]
from apps.core.controllers.[[ model | snake_case ]]_controller import [[ model ]]Controller
[% endfor -%]