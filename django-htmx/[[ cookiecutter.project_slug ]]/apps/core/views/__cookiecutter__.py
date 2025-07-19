[%- for model, model_values in cookiecutter._models.items() -%]
from apps.shared.views.abstracts import HtmxCrudViewWrapper
from apps.core.models import [[ model ]]
from apps.core.forms import [[ model ]]Form
from django.db.models import QuerySet


class _ViewWrapper(HtmxCrudViewWrapper):
    model = [[ model ]]
    form_class = [[ model ]]Form
    fields_table = [
        [% for field, field_values in model_values.fields.items() -%]
      '[[ field ]]',
    [% endfor -%]
    ]

    def search(self, search: str, queryset: QuerySet) -> QuerySet:
        return queryset.filter(name__icontains=search)

_view_wrapper = _ViewWrapper()
[[ model ]]ListView = _view_wrapper.get_list_view()
[[ model ]]CreateView = _view_wrapper.get_create_view()
[[ model ]]UpdateView = _view_wrapper.get_update_view()
[[ model ]]DeleteView = _view_wrapper.get_delete_view()
[[ model ]]DetailView = _view_wrapper.get_detail_view()

### NEEDLE: apps/core/views/[[ model | snake_case ]]_view.py
[% endfor -%]
