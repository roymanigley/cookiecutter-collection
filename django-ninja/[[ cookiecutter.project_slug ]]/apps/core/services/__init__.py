[%- for model in cookiecutter._models -%]
from apps.core.services.[[ model | snake_case ]]_service import [[ model ]]Service
[% endfor -%]
