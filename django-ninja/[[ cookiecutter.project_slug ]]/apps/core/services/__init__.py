[%- for model in cookiecutter.models.split(' ') -%]
from apps.core.services.[[ model | snake_case ]]_service import [[ model ]]Service
[% endfor -%]
