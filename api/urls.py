from django.urls import include, path, re_path
from django.contrib import admin
from rest_framework import routers
from rest_framework_jwt.views import refresh_jwt_token, verify_jwt_token
from catalog import views as catalog
from django_saml2_auth import views as sso

router = routers.DefaultRouter()
router.register(r"users", catalog.UserViewSet)
router.register(r"catalog/contact-types", catalog.ContactTypeViewSet)
router.register(r"catalog/data-fields", catalog.DataFieldViewSet)
router.register(r"catalog/data-objects", catalog.DataObjectViewSet)
router.register(r"catalog/data-object-types", catalog.DataObjectTypeViewSet)
router.register(r"catalog/data-schemas", catalog.DataSchemaViewSet)
router.register(r"catalog/data-sources", catalog.DataSourceViewSet)
router.register(r"catalog/data-source-types", catalog.DataSourceTypeViewSet)
router.register(
    r"catalog/data-source-types-params", catalog.DataSourceTypeParamsViewSet
)

urlpatterns = [
    path("sso/", include("django_saml2_auth.urls")),
    re_path(r"^jwt_refresh", refresh_jwt_token),
    re_path(r"^api-token-verify/", verify_jwt_token),
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
    # Overrides django's default and admin login
    path("accounts/login/", sso.signin),
    path("admin/login/", sso.signin),
]
