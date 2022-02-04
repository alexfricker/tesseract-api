from django.shortcuts import render
from rest_framework import viewsets, filters
from . import models
from . import serializers


class ContactTypeViewSet(viewsets.ModelViewSet):
    queryset = models.ContactType.objects.all()
    serializer_class = serializers.ContactTypeSerializer
    # TODO permission_classes = [permissions.IsAuthenticated]

class DataFieldViewSet(viewsets.ModelViewSet):
    queryset = models.DataField.objects.all()
    serializer_class = serializers.DataFieldSerializer
    # TODO permission_classes = [permissions.IsAuthenticated]

class DataObjectViewSet(viewsets.ModelViewSet):
    queryset = models.DataObject.objects.all()
    serializer_class = serializers.DataObjectSerializer
    # TODO permission_classes = [permissions.IsAuthenticated]

class DataObjectTypeViewSet(viewsets.ModelViewSet):
    queryset = models.DataObjectType.objects.all()
    serializer_class = serializers.DataObjectTypeSerializer
    # TODO permission_classes = [permissions.IsAuthenticated]

class DataSchemaViewSet(viewsets.ModelViewSet):
    queryset = models.DataSchema.objects.all()
    serializer_class = serializers.DataSchemaSerializer
    # TODO permission_classes = [permissions.IsAuthenticated]

class DataSourceViewSet(viewsets.ModelViewSet):
    queryset = models.DataSource.objects.all()
    serializer_class = serializers.DataSourceSerializer
    # TODO permission_classes = [permissions.IsAuthenticated]

class DataSourceTypeViewSet(viewsets.ModelViewSet):
    queryset = models.DataSourceType.objects.all()
    serializer_class = serializers.DataSourceTypeSerializer
    # TODO permission_classes = [permissions.IsAuthenticated]

class DataSourceTypeParamsViewSet(viewsets.ModelViewSet):
    queryset = models.DataSourceTypeParams.objects.all()
    serializer_class = serializers.DataSourceTypeParamsSerializer
    # TODO permission_classes = [permissions.IsAuthenticated]
