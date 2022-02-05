from rest_framework import serializers
from . import models


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Event
        fields = "__all__"


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Job
        fields = "__all__"


class JobExecutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.JobExecution
        fields = "__all__"


class JobScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.JobSchedule
        fields = "__all__"


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Step
        fields = "__all__"


class StepExecutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StepExecution
        fields = "__all__"


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Task
        fields = "__all__"


class TaskExecutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TaskExecution
        fields = "__all__"
