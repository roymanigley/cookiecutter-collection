[%- for model in cookiecutter._models -%]
from django.contrib.auth.mixins import PermissionRequiredMixin
from apps.core.models import [[ model ]]
from apps.core.forms import [[ model ]]Form
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class [[ model ]]ListView(PermissionRequiredMixin, ListView):
    template_name = 'crud/list.html'
    queryset = [[ model ]].objects.all()
    paginate_by = settings.DEFAULT_PAGE_SIZE
    context_object_name = 'records'
    permission_required = 'list_[[ model | lower]]'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = _('[[ model ]]')
        context['table_display_fields'] = [[ model]]Form.Meta.table_display_fields
        return context

class [[ model ]]UpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'crud/create-edit.html'
    form_class = [[ model]]Form
    queryset = [[ model ]].objects.all()
    success_url = '/[[ model | kebab_case]]'
    permission_required = 'change_[[ model | lower]]'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = _('[[ model ]]')
        return context


class [[ model ]]CreateView(PermissionRequiredMixin, CreateView):
    template_name = 'crud/create-edit.html'
    form_class = [[ model ]]Form
    queryset = [[ model ]].objects.all()
    success_url = '/[[ model | kebab_case]]'
    permission_required = 'create_[[ model | lower]]'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = _('[[ model ]]')
        return context


class [[ model ]]DeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'crud/delete.html'
    queryset = [[ model ]].objects.all()
    success_url = '/[[ model | kebab_case]]'
    permission_required = 'delete_[[ model | lower]]'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = _('[[ model ]]')
        return context
### NEEDLE: apps/core/views/[[ model | snake_case ]]_view.py
[% endfor -%]
