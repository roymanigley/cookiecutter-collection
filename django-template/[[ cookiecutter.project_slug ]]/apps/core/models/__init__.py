[%- for model in cookiecutter._models -%]
from apps.core.models.[[ model | snake_case ]] import [[ model ]]
[% endfor -%]
