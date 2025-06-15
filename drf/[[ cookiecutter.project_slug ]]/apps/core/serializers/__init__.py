[%- for model in cookiecutter._models -%]
from apps.core.serializers.[[ model | snake_case ]]_serializer import [[ model ]]Serializer
[% endfor %]
