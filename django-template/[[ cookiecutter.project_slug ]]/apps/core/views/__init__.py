[%- for model in cookiecutter._models -%]
from apps.core.views.[[ model | snake_case ]]_view import [[ model ]]ListView, \
        [[ model ]]UpdateView, \
        [[ model ]]CreateView, \
        [[ model ]]DeleteView
[% endfor -%]
