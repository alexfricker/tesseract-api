from rest_framework import serializers
from . import models


class ContactTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ContactType
        fields = "__all__"

class DataFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DataField
        fields = "__all__"

class DataObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DataObject
        fields = "__all__"

class DataObjectTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DataObjectType
        fields = "__all__"

class DataSchemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DataSchema
        fields = "__all__"

class DataSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DataSource
        fields = "__all__"

class DataSourceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DataSourceType
        fields = "__all__"

class DataSourceTypeParamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DataSourceTypeParams
        fields = "__all__"
