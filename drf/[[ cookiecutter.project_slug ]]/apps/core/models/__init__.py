[%- for model in cookiecutter.models.split(' ') -%]
from apps.core.models.[[ model | snake_case]] import [[ model ]]
[% endfor %]
