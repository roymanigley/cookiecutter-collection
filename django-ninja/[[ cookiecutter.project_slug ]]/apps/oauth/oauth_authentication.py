from oauth2_provider.models import AccessToken
from ninja_extra.security import HttpBearer
from django.http import HttpRequest
from ninja_extra.exceptions import PermissionDenied


class OAuth2(HttpBearer):
    def authenticate(self, request: HttpRequest, token: str):
        try:
            access_token = AccessToken.objects.select_related(
                'user'
            ).select_related(
                'application__user'
            ).get(
                token=token
            )
            if access_token.is_expired():
                return None
            user = access_token.user
            if user is None:
                user = access_token.application.user
            if user is None:
                raise PermissionDenied(
                    f'No User is assigned to the Token'
                )
            if not user.is_active:
                raise PermissionDenied(
                    f'The User {user} is not active'
                )
            access_token.user = user
            return access_token
        except AccessToken.DoesNotExist:
            return None


class OAuth2Async(HttpBearer):
    async def authenticate(self, request: HttpRequest, token: str):
        try:
            access_token = await AccessToken.objects.select_related(
                'user'
            ).select_related(
                'application__user'
            ).aget(
                token=token
            )
            if access_token.is_expired():
                return None
            user = access_token.user
            if user is None:
                user = access_token.application.user
            if user is None:
                raise PermissionDenied(
                    f'No User is assigned to the Token'
                )
            if not user.is_active:
                raise PermissionDenied(
                    f'The User {user} is not active'
                )
            access_token.user = user
            return access_token
        except AccessToken.DoesNotExist:
            return None
