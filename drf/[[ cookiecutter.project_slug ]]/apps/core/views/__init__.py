[%- for model in cookiecutter.models.split(' ') -%]
from apps.core.views.[[ model | snake_case ]]_view import [[ model ]]ViewSet
[% endfor %]
