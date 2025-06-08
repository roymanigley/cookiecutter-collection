from ninja.errors import ValidationError
from django.http import JsonResponse

def exception_handler(request, exc):
    if isinstance(exc, ValidationError):
        status_code = 422
        message = exc.errors
    elif hasattr(exc, 'status_code'):
        status_code = exc.status_code
        message = str(exc)
    else:
        status_code = 500
        message = str(exc)

    return JsonResponse({
        "message": message,
        "status": status_code,
        "path": request.path,
    }, status=status_code)