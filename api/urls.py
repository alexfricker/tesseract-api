
from django.urls import include, path, re_path
from django.contrib import admin
from rest_framework import routers
from rest_framework_jwt.views import refresh_jwt_token
from catalog import views as catalog
from django_saml2_auth import views as sso

router = routers.DefaultRouter()
router.register(r"user", catalog.ContactTypeViewSet)
router.register(r"contact-types", catalog.ContactTypeViewSet)
router.register(r"data-fields", catalog.DataFieldViewSet)
router.register(r"data-objects", catalog.DataObjectViewSet)
router.register(r"data-object-types", catalog.DataObjectTypeViewSet)
router.register(r"data-schemas", catalog.DataSchemaViewSet)
router.register(r"data-sources", catalog.DataSourceViewSet)
router.register(r"data-source-types", catalog.DataSourceTypeViewSet)
router.register(r"data-source-types-params", catalog.DataSourceTypeParamsViewSet)

urlpatterns = [
    path("sso/", include("django_saml2_auth.urls")),
    re_path(r'^jwt_refresh', refresh_jwt_token),
    path("", include(router.urls)),
    path("admin/", admin.site.urls),

    # Overrides django's default and admin login
    path('accounts/login/', sso.signin),
    path('admin/login/', sso.signin),
]