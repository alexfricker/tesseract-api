from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, filters, permissions
from django.contrib.auth.models import User
from django_saml2_auth import views
from . import models
from . import serializers

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class ContactTypeViewSet(viewsets.ModelViewSet):
    queryset = models.ContactType.objects.all()
    serializer_class = serializers.ContactTypeSerializer

class DataFieldViewSet(viewsets.ModelViewSet):
    queryset = models.DataField.objects.all()
    serializer_class = serializers.DataFieldSerializer

class DataObjectViewSet(viewsets.ModelViewSet):
    queryset = models.DataObject.objects.all()
    serializer_class = serializers.DataObjectSerializer

class DataObjectTypeViewSet(viewsets.ModelViewSet):
    queryset = models.DataObjectType.objects.all()
    serializer_class = serializers.DataObjectTypeSerializer

class DataSchemaViewSet(viewsets.ModelViewSet):
    queryset = models.DataSchema.objects.all()
    serializer_class = serializers.DataSchemaSerializer

class DataSourceViewSet(viewsets.ModelViewSet):
    queryset = models.DataSource.objects.all()
    serializer_class = serializers.DataSourceSerializer

class DataSourceTypeViewSet(viewsets.ModelViewSet):
    queryset = models.DataSourceType.objects.all()
    serializer_class = serializers.DataSourceTypeSerializer

class DataSourceTypeParamsViewSet(viewsets.ModelViewSet):
    queryset = models.DataSourceTypeParams.objects.all()
    serializer_class = serializers.DataSourceTypeParamsSerializer
