from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers
from rest_framework_jwt.views import refresh_jwt_token
from catalog import views as catalog
from django_saml2_auth import views as sso

router = routers.DefaultRouter()
router.register(r"contact-types", catalog.ContactTypeViewSet)
router.register(r"data-fields", catalog.DataFieldViewSet)
router.register(r"data-objects", catalog.DataObjectViewSet)
router.register(r"data-object-types", catalog.DataObjectTypeViewSet)
router.register(r"data-schemas", catalog.DataSchemaViewSet)
router.register(r"data-sources", catalog.DataSourceViewSet)
router.register(r"data-source-types", catalog.DataSourceTypeViewSet)
router.register(r"data-source-types-params", catalog.DataSourceTypeParamsViewSet)

urlpatterns = [
    url(r'^sso/', include('django_saml2_auth.urls')),
    url(r'^jwt_refresh', refresh_jwt_token),
    path("", include(router.urls)),

    # Overrides django's default and admin login
    path('accounts/login/', sso.views.signin),
    path('admin/login/', sso.views.signin),
]