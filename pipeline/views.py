from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers


class EventViewSet(viewsets.ModelViewSet):
    queryset = models.Event.objects.all().order_by("id")
    serializer_class = serializers.EventSerializer


class JobViewSet(viewsets.ModelViewSet):
    queryset = models.Job.objects.all().order_by("id")
    serializer_class = serializers.JobSerializer


class JobExecutionViewSet(viewsets.ModelViewSet):
    queryset = models.JobExecution.objects.all().order_by("id")
    serializer_class = serializers.JobExecutionSerializer


class JobScheduleViewSet(viewsets.ModelViewSet):
    queryset = models.JobSchedule.objects.all().order_by("id")
    serializer_class = serializers.JobScheduleSerializer


class StepViewSet(viewsets.ModelViewSet):
    queryset = models.Step.objects.all().order_by("id")
    serializer_class = serializers.StepSerializer


class StepExecutionViewSet(viewsets.ModelViewSet):
    queryset = models.StepExecution.objects.all().order_by("id")
    serializer_class = serializers.StepExecutionSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = models.Task.objects.all().order_by("id")
    serializer_class = serializers.TaskSerializer


class TaskExecutionViewSet(viewsets.ModelViewSet):
    queryset = models.TaskExecution.objects.all().order_by("id")
    serializer_class = serializers.TaskExecutionSerializer
