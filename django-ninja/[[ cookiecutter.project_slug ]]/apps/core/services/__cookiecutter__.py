[%- for model in cookiecutter._models -%]
from ninja_extra import ModelService


class [[ model ]]Service(ModelService):
    pass
### NEEDLE: apps/core/services/[[ model | snake_case ]]_service.py
[% endfor -%]