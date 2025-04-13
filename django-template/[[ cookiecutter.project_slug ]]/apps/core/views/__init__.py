[%- for model in cookiecutter.models.split(' ') -%]
from apps.core.views.[[ model | snake_case ]]_view import [[ model ]]ListView, \
        [[ model ]]UpdateView, \
        [[ model ]]CreateView, \
        [[ model ]]DeleteView
[% endfor -%]
