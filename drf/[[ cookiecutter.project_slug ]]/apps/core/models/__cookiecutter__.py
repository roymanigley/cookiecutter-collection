[%- for model in cookiecutter.models.split(' ') -%]
from apps.core.models.abstracts import AuditableModel
from django.db.models import QuerySet, Manager


class _QuerySet(QuerySet['[[ model ]]']):
    pass


class _Manager(Manager):
    def get_queryset(self) -> _QuerySet['[[ model ]]']:
        return _QuerySet(model=self.model, using=self._db)


class [[ model ]](AuditableModel):

    objects = _Manager()

    def __str__(self) -> str:
        return f'{self}'

    class Meta:
        ordering = ['id']
### NEEDLE: apps/core/models/[[ model | snake_case ]].py
[% endfor -%]
