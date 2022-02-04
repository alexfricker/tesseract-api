from datetime import datetime
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.db.models.deletion import CASCADE

# ENUMS:
class DataSourceType(models.Model):
    ### Postgres, Salesforce, API, Flat File, etc ###
    name = models.CharField(max_length=50, unique=True)
    is_scannable = models.BooleanField(default=False)
    image_name = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class DataSourceTypeParams(models.Model):
    source_type = models.ForeignKey(DataSourceType, on_delete=CASCADE)
    name = models.CharField(max_length=50)
    required = models.BooleanField(default=True)

    def __str__(self):
        return self.source_type.name + " - " + self.name

    class Meta:
        unique_together = [["source_type", "name"]]


class DataObjectType(models.Model):
    ### CSV, JSON, XML, SQL Server Table, SQL Server View, etc ###
    data_source_type = models.ForeignKey(DataSourceType, on_delete=CASCADE)
    name = models.CharField(max_length=50)
    is_scannable = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)

    class Meta:
        unique_together = [["data_source_type", "name"]]

    def __str__(self):
        return self.name


class ContactType(models.Model):
    ### technical owner, business owner, etc ###
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


# MODELS:
class DataSource(models.Model):
    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=20, unique=True)
    type = models.ForeignKey(DataSourceType, on_delete=models.PROTECT)
    description = models.TextField(blank=True, null=True)
    is_phi = models.BooleanField(default=False)
    is_sensitive = models.BooleanField(default=False)
    is_public_domain = models.BooleanField(default=False)

    def __str__(self):
        return self.short_name


class DataObject(models.Model):
    data_source = models.ForeignKey(DataSource, on_delete=models.CASCADE)
    type = models.ForeignKey(DataObjectType, on_delete=models.PROTECT)
    schema_name = models.CharField(max_length=100, blank=True, null=True)
    object_name = models.CharField(max_length=400)
    full_name = models.CharField(max_length=400)
    friendly_name = models.CharField(max_length=250, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_phi = models.BooleanField(default=False)
    is_sensitive = models.BooleanField(default=False)
    is_public_domain = models.BooleanField(default=False)
    scan_datetime_utc = models.DateTimeField(blank=True, null=True)

    class Meta:
        unique_together = [["data_source", "full_name"]]


class DataSchema(models.Model):
    created_date_utc = models.DateTimeField(default=datetime.utcnow)
    data_object = models.ForeignKey(DataObject, on_delete=CASCADE)
    schema_version = models.IntegerField(default=1)
    schema_json = models.TextField(blank=True, null=True)


class DataField(models.Model):
    data_schema = models.ForeignKey(DataSchema, on_delete=CASCADE)
    field_name = models.CharField(max_length=800)
    description = models.TextField(blank=True, null=True)
    orig_data_type = models.CharField(max_length=200)
    univ_data_type = models.CharField(max_length=200)
    max_length = models.IntegerField(blank=True, null=True)
    scale = models.IntegerField(blank=True, null=True)
    precision = models.IntegerField(blank=True, null=True)
    is_nullable = models.BooleanField(default=True)
    is_calculated = models.BooleanField(default=False)
    is_primary_key = models.BooleanField(default=False)

    class Meta:
        unique_together = [["data_schema", "field_name"]]


class DataSourceContact(models.Model):
    contact_type = models.ForeignKey(ContactType, on_delete=models.PROTECT)
    data_source = models.ForeignKey(DataSource, on_delete=models.CASCADE)
    contact_name = models.CharField(max_length=200)
    contact_email = models.CharField(max_length=200, blank=True, null=True)


class Tag(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=CASCADE)
    object_id = models.IntegerField()
    tag = models.CharField(max_length=25)

    class Meta:
        unique_together = [["content_type", "object_id", "tag"]]

    def __str__(self):
        return self.tag
