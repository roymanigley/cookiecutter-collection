[%- for model in cookiecutter.models.split(' ') -%]
from rest_framework import serializers
from apps.core import models


class [[ model ]]Serializer(serializers.ModelSerializer):

    class Meta:
        model = models.[[ model ]]
        fields = '__all__'
### NEEDLE: apps/core/serializers/[[ model | snake_case ]]_serializer.py
[% endfor -%]
