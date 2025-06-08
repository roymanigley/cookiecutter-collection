[%- for model in cookiecutter.models.split(' ') -%]
from apps.core.schemas.[[ model | snake_case ]]_schema import [[ model ]]RetrieveSchema, [[ model ]]CreateSchema
[% endfor -%]
