from ninja_extra.exceptions import PermissionDenied

class ScopableControllerMixin:
    
    authorized_scopes = {
        'GET': [],
        'POST': [],
        'PUT': [],
        'PATCH': [],
        'DELETE': [],
    }

    def check_permissions(self):

        required_scopes: list[str] = self.authorized_scopes.get(
            self.context.request.method
        )
        if required_scopes:
            token = getattr(self.context.request, "auth", None)
            valid_scope = False
            for scope in required_scopes:
                if token and scope in token.scope.split(' '):
                    valid_scope = True
                    continue
            if not valid_scope:
                self.permission_denied
                raise PermissionDenied(
                    402, f"Missing one of the required scopes: {required_scopes}"
                )

        return super().check_permissions()

    async def async_check_permissions(self):

        required_scopes: list[str] = await self.authorized_scopes.aget(
            self.context.request.method
        )
        if required_scopes:
            token = getattr(self.context.request, "auth", None)
            valid_scope = False
            for scope in required_scopes:
                if token and scope in token.scope.split(' '):
                    valid_scope = True
                    continue
            if not valid_scope:
                self.permission_denied
                raise PermissionDenied(
                    402, f"Missing one of the required scopes: {required_scopes}"
                )

        return super().async_check_permissions()
