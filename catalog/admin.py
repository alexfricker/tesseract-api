from django.contrib import admin
from . import models


admin.site.register(models.ContactType)
admin.site.register(models.DataField)
admin.site.register(models.DataObject)
admin.site.register(models.DataObjectType)
admin.site.register(models.DataSchema)
admin.site.register(models.DataSource)
admin.site.register(models.DataSourceType)
admin.site.register(models.DataSourceTypeParams)