from django.urls import include, path
from rest_framework import routers
from catalog import views as catalog

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
    path("", include(router.urls)),
]