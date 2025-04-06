[%- for model in cookiecutter.models.split(' ') -%]
from rest_framework.viewsets import ModelViewSet
from apps.core.models import [[ model ]]
from apps.core.serializers import [[ model ]]Serializer


class [[ model ]]ViewSet(ModelViewSet):
    queryset = [[ model ]].objects.all()
    serializer_class = [[ model ]]Serializer
    required_alternate_scopes = {
        [% raw -%]
        'GET': [['read']],
        'POST': [['create']],
        'PUT': [['update']],
        'DELETE': [['delete']],
        [% endraw %]
    }
### NEEDLE: apps/core/views/[[ model | snake_case ]]_view.py
[% endfor -%]

