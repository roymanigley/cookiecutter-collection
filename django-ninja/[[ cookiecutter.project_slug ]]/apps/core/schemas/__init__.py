[%- for model in cookiecutter._models -%]
from apps.core.schemas.[[ model | snake_case ]]_schema import [[ model ]]RetrieveSchema, [[ model ]]CreateSchema
[% endfor -%]
