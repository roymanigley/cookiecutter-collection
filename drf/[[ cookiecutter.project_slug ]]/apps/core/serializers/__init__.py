[%- for model in cookiecutter.models.split(' ') -%]
from apps.core.serializers.[[ model | snake_case ]]_serializer import [[ model ]]Serializer
[% endfor %]
