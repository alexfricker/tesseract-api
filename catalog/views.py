from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, filters, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from django.contrib.auth.models import User
from django_saml2_auth import views
from . import models
from pipeline import models as pipeline
from . import serializers
from pipeline import serializers as p_serializers


def SwaggerUI(request): #TODO: move this into UI
    return render(request, "catalog/swagger-ui.html")

@api_view(('GET',))
def Search(request): # TODO: move this somewhere else and make better (use a search engine)
    query = request.GET.get("query", None)
    data_srcs_query = models.DataSource.objects.all()
    data_objs_query = models.DataObject.objects.all()
    jobs_query = pipeline.Job.objects.all()

    if query:
         data_srcs_query = data_srcs_query.filter(name__icontains=query).all()[:5]
         data_objs_query = data_objs_query.filter(full_name__icontains=query).all()[:5]
         jobs_query = jobs_query.filter(name__icontains=query).all()[:5]

    return Response({"data_srcs": serializers.DataSourceSerializer(data_srcs_query, many=True).data,
        "data_objs": serializers.DataObjectSerializer(data_objs_query, many=True).data,
        "jobs": p_serializers.JobSerializer(jobs_query, many=True).data})


class UserViewSet(viewsets.ModelViewSet): # TODO: move this somewhere else
    queryset = User.objects.all().order_by("id")
    serializer_class = serializers.UserSerializer


class ContactTypeViewSet(viewsets.ModelViewSet):
    queryset = models.ContactType.objects.all().order_by("id")
    serializer_class = serializers.ContactTypeSerializer


class DataFieldViewSet(viewsets.ModelViewSet):
    queryset = models.DataField.objects.all().order_by("id")
    serializer_class = serializers.DataFieldSerializer


class DataObjectViewSet(viewsets.ModelViewSet):
    queryset = models.DataObject.objects.all().order_by("id")
    serializer_class = serializers.DataObjectSerializer


class DataObjectTypeViewSet(viewsets.ModelViewSet):
    queryset = models.DataObjectType.objects.all().order_by("id")
    serializer_class = serializers.DataObjectTypeSerializer


class DataSchemaViewSet(viewsets.ModelViewSet):
    queryset = models.DataSchema.objects.all().order_by("id")
    serializer_class = serializers.DataSchemaSerializer


class DataSourceViewSet(viewsets.ModelViewSet):
    queryset = models.DataSource.objects.all().order_by("id")
    serializer_class = serializers.DataSourceSerializer


class DataSourceTypeViewSet(viewsets.ModelViewSet):
    queryset = models.DataSourceType.objects.all().order_by("id")
    serializer_class = serializers.DataSourceTypeSerializer


class DataSourceTypeParamsViewSet(viewsets.ModelViewSet):
    queryset = models.DataSourceTypeParams.objects.all().order_by("id")
    serializer_class = serializers.DataSourceTypeParamsSerializer
