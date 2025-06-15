[%- for model in cookiecutter._models -%]
from apps.core.schemas import [[model]]RetrieveSchema, [[model]]CreateSchema
from apps.core.models import [[model]]
from apps.core.services import [[model]]Service
from apps.core.controllers.abstracts import ScopableControllerMixin
from ninja_extra import (
    ModelControllerBase,
    ModelConfig,
    api_controller
)


@api_controller('[[ model | kebab_case]]s', tags=['[[ model ]]s'])
class [[model]]Controller(ScopableControllerMixin, ModelControllerBase):
    service_type = [[model]]Service
    model_config = ModelConfig(
        model=[[model]],
        create_schema=[[model]]CreateSchema,
        retrieve_schema=[[model]]RetrieveSchema,
        update_schema=[[model]]CreateSchema,
        async_routes=[[cookiecutter.async ]]
    )
    authorized_scopes = {
        'GET': ['[[ model | snake_case ]]_read'],
        'POST': ['[[ model | snake_case ]]_create'],
        'PUT': ['[[ model | snake_case ]]_update'],
        'PATCH': ['[[ model | snake_case ]]_update'],
        'DELETE': ['[[ model | snake_case ]]_delete'],
    }
### NEEDLE: apps/core/controllers/[[ model | snake_case ]]_controller.py
[% endfor -%]
