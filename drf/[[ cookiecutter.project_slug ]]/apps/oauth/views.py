from rest_framework import status
from django.http import JsonResponse


def not_found_view(request, *args, **kwargs):
    return JsonResponse(
        data={'detail': 'Not found'},
        status=status.HTTP_404_NOT_FOUND
    )
