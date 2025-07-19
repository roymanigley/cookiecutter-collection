[%- for model in cookiecutter._models -%]
from apps.core.views.[[ model | snake_case ]]_view import \
    [[ model ]]ListView, \
    [[ model ]]CreateView, \
    [[ model ]]UpdateView, \
    [[ model ]]DeleteView, \
    [[ model ]]DetailView
[% endfor -%]
