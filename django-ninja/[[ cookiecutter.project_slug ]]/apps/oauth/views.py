from django.http import JsonResponse


def not_found_view(request, *args, **kwargs):
    return JsonResponse(
        data={'detail': 'Not found'},
        status=404
    )
