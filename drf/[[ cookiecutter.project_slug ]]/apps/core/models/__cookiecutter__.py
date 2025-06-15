[%- for model, model_values in cookiecutter._models.items() -%]
from django.db import models
from django.db.models import QuerySet, Manager
from apps.core.models.abstracts import AuditableModel


class _QuerySet(models.QuerySet):

    def search(self, search: str) -> '_QuerySet[["["]][[ model ]][["]"]]':
        if search is not None:
            return self.filter([[ model_values.fields|first ]]__icontains=search)
        return self


class _Manager(models.Manager):

    def get_queryset(self) -> _QuerySet['[[ model ]]']:
        return _QuerySet(model=self.model, using=self._db)

    def search(self, search: str) -> _QuerySet['[[ model ]]']:
        return self.get_queryset().search(search)


class [[ model ]](AuditableModel):
    [% for field, field_values in model_values.fields.items() -%]
    [[ field|as_model_field(field_values) ]]
    [% endfor %]
    objects = _Manager()

    def __str__(self) -> str:
        return f'{self.[[ model_values.fields|first ]]}'

    class Meta:
        ordering = ['[[ model_values.fields|first ]]']

### NEEDLE: apps/core/models/[[ model | snake_case ]].py
[% endfor -%]
