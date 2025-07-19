from typing import Optional

from django.template import Library

from apps.authentication.models import UserProfile

register = Library()

@register.filter('get_attr')
def get_attr(obj: any, attr: str, empty_str_instead_of_none: bool = True) -> Optional[any]:
    value = None
    if obj and isinstance(obj, dict):
        value = obj.get(attr)
    elif obj and hasattr(obj, attr):
        value = getattr(obj, attr)
    if value is None and empty_str_instead_of_none:
        value = ''
    return value

@register.filter('range')
def get_attr(start: int, end: int) -> list[int]:
    return list(range(start, end))

@register.filter('to_dict')
def to_dict(obj: any) -> dict:
    return obj.__dict__

@register.filter('is_authenticated')
def is_authenticated(user: UserProfile) -> bool:
    return bool(user and user.is_authenticated)

@register.filter('has_perm')
def has_permission(user: UserProfile, permission: str) -> bool:
    return user.has_perm(permission)
