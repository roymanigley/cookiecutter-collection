from django import forms
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.db import models
from django.db.models import QuerySet
from django.http import HttpResponse, HttpRequest
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, View, TemplateView, FormView
from django.shortcuts import render


def is_htmx_request(request: HttpRequest) -> bool:
    return request.headers.get('HX-Request') is not None


class HtmxTemplateView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_htmx'] = is_htmx_request(self.request)
        return context


class HtmxTemplateViewLoginRequired(LoginRequiredMixin, HtmxTemplateView):
    pass


class HtmxTemplateViewPermissionRequired(PermissionRequiredMixin, HtmxTemplateView):
    pass


class HtmxFormView(FormView):

    def form_valid(self, form: forms.ModelForm) -> HttpResponse:
        response = super().form_valid(form)
        if is_htmx_request(self.request):
            return render(self.request, 'components/crud/success.html', {'object': None, 'is_htmx': True})
        return response

    def form_invalid(self, form: forms.ModelForm) -> HttpResponse:
        if is_htmx_request(self.request):
            return self.render_to_response(
                self.get_context_data(form=form),
                status=400
            )
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_htmx'] = is_htmx_request(self.request)
        return context


class HtmxFormViewLoginRequired(LoginRequiredMixin, HtmxFormView):
    pass


class HtmxFormViewPermissionRequired(PermissionRequiredMixin, HtmxFormView):
    pass


class HtmxCrudViewWrapper:

    paginate_by: int = 10
    model: models.Model = None
    fields_detail: list[str] = None
    fields_table: list[str] = None
    form_class: forms.ModelForm = None

    def __init__(self):
        errors = []
        if self.model is None:
            errors.append(f'"model" is required on {self.__class__.__name__}')
        if self.form_class is None:
            errors.append(
                f'"form_class" is required on {self.__class__.__name__}')
        if self.fields_table is None and self.fields_detail is None:
            errors.append(
                f'either "table_fields" or "detail_field" is required on {self.__class__.__name__}')

        assert not errors, '\n - ' + '\n - '.join(errors)

    def get_queryset(self, view: View) -> QuerySet:
        return self.model.objects.all()

    def search(self, search: str, queryset: QuerySet) -> QuerySet:
        return queryset.all()

    def get_list_view(self_wrapper) -> type[ListView]:
        class HtmxListView(PermissionRequiredMixin, ListView):
            template_name = 'components/crud/table/table.html'
            paginate_by = self_wrapper.paginate_by
            permission_required = f'core.view_{self_wrapper.model.__name__}'.lower()

            def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                if self_wrapper.fields_table:
                    context['fields'] = self_wrapper.fields_table
                else:
                    context['fields'] = self_wrapper.fields_detail
                context['is_htmx'] = is_htmx_request(self.request)
                return context

            def get_queryset(self):
                queryset = self_wrapper.get_queryset(self)
                if search := self.request.GET.get('search'):
                    queryset = self_wrapper.search(search, queryset)
                if order_by := self.request.GET.get('order_by'):
                    queryset = queryset.order_by(order_by)
                return queryset.all()

        return HtmxListView

    def get_create_view(self_wrapper) -> type[CreateView]:
        class HtmxCreateView(PermissionRequiredMixin, CreateView):
            template_name = 'components/crud/create/create.html'
            form_class = self_wrapper.form_class
            permission_required = f'core.add_{self_wrapper.model.__name__}'.lower()

            def form_valid(self, form: forms.ModelForm) -> HttpResponse:
                response = super().form_valid(form)
                if is_htmx_request(self.request):
                    return render(self.request, 'components/crud/success.html', {'object': self.object, 'is_htmx': True})
                return response

            def form_invalid(self, form: forms.ModelForm) -> HttpResponse:
                if is_htmx_request(self.request):
                    return self.render_to_response(
                        self.get_context_data(form=form),
                        status=400
                    )
                return super().form_invalid(form)

            def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                context['is_htmx'] = is_htmx_request(self.request)
                return context

            def get_success_url(self) -> str:
                return f'/{self.object.id}/'

        return HtmxCreateView

    def get_update_view(self_wrapper) -> type[UpdateView]:
        class HtmxUpdateView(PermissionRequiredMixin, UpdateView):
            template_name: str = 'components/crud/edit/edit.html'
            form_class: forms.ModelForm = self_wrapper.form_class
            permission_required = f'core.change_{self_wrapper.model.__name__}'.lower()

            def form_valid(self, form: forms.ModelForm) -> HttpResponse:
                response = super().form_valid(form)
                if is_htmx_request(self.request):
                    return render(self.request, 'components/crud/success.html', {'object': self.object, 'is_htmx': True})
                return response

            def form_invalid(self, form: forms.ModelForm) -> HttpResponse:
                if is_htmx_request(self.request):
                    return self.render_to_response(
                        self.get_context_data(form=form),
                        status=400
                    )
                return super().form_invalid(form)

            def get_queryset(self):
                return self_wrapper.get_queryset(self)

            def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                context['is_htmx'] = is_htmx_request(self.request)
                return context

            def get_success_url(self) -> str:
                return f'/{self.object.id}/'

        return HtmxUpdateView

    def get_delete_view(self_wrapper) -> type[DeleteView]:
        class HtmxDeleteView(PermissionRequiredMixin, DeleteView):
            template_name = 'components/crud/delete/delete.html'
            permission_required = f'core.delete_{self_wrapper.model.__name__}'.lower()

            def form_valid(self, form: forms.ModelForm) -> HttpResponse:
                response = super().form_valid(form)
                if is_htmx_request(self.request):
                    return render(self.request, 'components/crud/success.html', {'object': None, 'is_htmx': True})
                return response

            def form_invalid(self, form: forms.ModelForm) -> HttpResponse:
                if is_htmx_request(self.request):
                    return self.render_to_response(
                        self.get_context_data(form=form),
                        status=400
                    )
                return super().form_invalid(form)

            def get_queryset(self):
                return self_wrapper.get_queryset(self)

            def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                context['is_htmx'] = is_htmx_request(self.request)
                return context

            def get_success_url(self) -> str:
                return '../'

        return HtmxDeleteView

    def get_detail_view(self_wrapper) -> type[DetailView]:
        class HtmxDetailView(PermissionRequiredMixin, DetailView):
            template_name = 'components/crud/detail/detail.html'
            permission_required = f'core.view_{self_wrapper.model.__name__}'.lower()

            def get_queryset(self):
                return self_wrapper.get_queryset(self)

            def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                if self_wrapper.fields_detail:
                    context['fields'] = self_wrapper.fields_detail
                else:
                    context['fields'] = self_wrapper.fields_table
                context['is_htmx'] = is_htmx_request(self.request)
                return context

        return HtmxDetailView