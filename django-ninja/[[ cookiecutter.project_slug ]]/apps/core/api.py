from ninja_extra import NinjaExtraAPI
from apps.core import controllers
from ninja import Redoc
from apps.oauth.oauth_authentication import [% if cookiecutter.async %]OAuth2Async[% else %]OAuth2[% endif %]
from apps.core.exceptions import exception_handler


ninja_api = NinjaExtraAPI(
    docs=Redoc(),
    auth=[% if cookiecutter.async %]OAuth2Async[% else %]OAuth2[% endif %](),
    openapi_extra={
        'info': {
            'description': '''
**This API uses OAuth 2**  

> `authorization url`: [/oauth/authorize/](/oauth/authorize/)  
> `token url`: [/oauth/token/](/oauth/token/)  
>  
> Create the Client:  
> - Authorization Flow: [/admin/oauth2_provider/application/add](/admin/oauth2_provider/application/add/?redirect_uris=http://localhost:8000/&authorization_grant_type=authorization-code&algorithm=HS256&client_type=public&client_secret=&name=app-client)  
> - Client Credentials Flow: [/admin/oauth2_provider/application/add](/admin/oauth2_provider/application/add/?redirect_uris=http://localhost:8000/&authorization_grant_type=client-credentials&algorithm=HS256&client_type=confidential&name=m2m-client)  
  
**Available Scopes:**
- `openid`: Open Id Connect
[% for model in cookiecutter.models.split(' ') %] 
`[[ model ]]`  
- `[[ model | snake_case ]]_read`: Read access for `[[ model ]]`
- `[[ model | snake_case ]]_create`: Create access for `[[ model ]]`
- `[[ model | snake_case ]]_update`: Update access for `[[ model ]]`
- `[[ model | snake_case ]]_delete`: Delete access for `[[ model ]]`  
[% endfor %]
''',
        },
    }
)


ninja_api.register_controllers(
    [% for model in cookiecutter.models.split(' ') -%]
    controllers.[[model]]Controller,
[% endfor %])

ninja_api.add_exception_handler(Exception, exception_handler)
