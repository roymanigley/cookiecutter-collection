[%- for model in cookiecutter.models.split(' ') -%]
from django.db.models import QuerySet, Manager
from apps.core.models.abstracts import AuditableModel
from django.db import models

class _QuerySet(QuerySet['[[ model ]]']):
    pass


class _Manager(Manager):
    def get_queryset(self) -> _QuerySet['[[ model ]]']:
        return _QuerySet(model=self.model, using=self._db)


class [[model]](AuditableModel):
    name = models.CharField(max_length=255)

    objects = _Manager()

    def __str__(self) -> str:
        return f'{self.name}'

    class Meta:
        ordering = ['id']
### NEEDLE: apps/core/models/[[ model | snake_case ]].py
[% endfor -%]
