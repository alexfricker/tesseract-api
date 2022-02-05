from django.contrib import admin
from . import models


admin.site.register(models.Event)
admin.site.register(models.Job)
admin.site.register(models.JobExecution)
admin.site.register(models.JobSchedule)
admin.site.register(models.Step)
admin.site.register(models.StepExecution)
admin.site.register(models.Task)
admin.site.register(models.TaskExecution)
