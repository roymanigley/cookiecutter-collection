from rest_framework.routers import DefaultRouter
from apps.core import views

router = DefaultRouter()
[% for model in cookiecutter._models -%]
router.register('[[ model | kebab_case ]]', views.[[ model ]]ViewSet)
[% endfor %]
urlpatterns = router.get_urls()
