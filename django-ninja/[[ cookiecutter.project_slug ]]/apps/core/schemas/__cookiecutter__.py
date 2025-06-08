[%- for model in cookiecutter.models.split(' ') -%]
from ninja_schema import ModelSchema
from apps.core.models import [[ model ]]


class [[ model ]]RetrieveSchema(ModelSchema):
    class Config:
        model = [[ model ]]
        model_fields = '__all__'


class [[ model ]]CreateSchema(ModelSchema):
    class Config:
        model = [[ model ]]
        model_fields = '__all__'
        exclude = ['created_at', 'created_by', 'updated_at', 'updated_by', 'id']

### NEEDLE: apps/core/schemas/[[ model | snake_case ]]_schema.py
[% endfor -%]