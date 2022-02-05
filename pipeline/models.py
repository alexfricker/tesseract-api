from datetime import datetime
from django.db import models
from django.db.models.deletion import CASCADE, RESTRICT
from catalog.models import DataSource, DataObject, DataField, DataSourceType


class Job(models.Model):
    """ex: [SQL DB] Full Metadata Scan"""

    data_source = models.ForeignKey(DataSource, on_delete=CASCADE)
    name = models.CharField(max_length=250)
    type = models.CharField(
        max_length=25
    )  # meta; raw; replicate; datavault; etc TODO: make enum
    is_enabled = models.BooleanField(default=True)
    parallelism_degree = models.IntegerField(default=1)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=25, default="new")

    class Meta:
        unique_together = [["data_source", "name"]]

    def __str__(self):
        return self.name


class JobSchedule(models.Model):
    job = models.ForeignKey(Job, on_delete=CASCADE)
    name = models.CharField(max_length=250)
    start_timestamp_utc = models.DateTimeField()
    end_timestamp_utc = models.DateTimeField(blank=True, null=True)
    chron_string = models.CharField(max_length=50)
    is_enabled = models.BooleanField(default=True)

    class Meta:
        db_table = "pipeline_job_schedule"

    def __str__(self):
        return f"{self.job} - {self.name}"


class JobExecution(models.Model):
    job = models.ForeignKey(Job, on_delete=CASCADE)
    unique_name = models.CharField(max_length=150, unique=True)
    created_timestamp_utc = models.DateTimeField(default=datetime.utcnow)
    start_timestamp_utc = models.DateTimeField(blank=True, null=True)
    end_timestamp_utc = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=50)  # submitted, starting, running, completed
    outcome = models.CharField(
        max_length=50, blank=True, null=True
    )  # null, succeeded, failed, partially succeeded
    error_level = models.CharField(max_length=50, blank=True, null=True)
    error_message = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "pipeline_job_execution"

    def __str__(self):
        return f"{self.job} - {self.unique_name}"


class Event(models.Model):
    job_execution = models.ForeignKey(JobExecution, on_delete=CASCADE)
    event_timestamp_utc = models.DateTimeField(default=datetime.utcnow)
    level = models.CharField(max_length=50)  # info, warning, error
    event_type = models.CharField(
        max_length=50
    )  # status change; exception; notification; etc
    message = models.TextField()
    # TODO: switch to generic - have content_type = job/step/task and object_id = pk of table


class Step(models.Model):
    """containers to create and command-line arguments"""

    job = models.ForeignKey(Job, related_name="steps", on_delete=CASCADE)
    name = models.CharField(max_length=250)
    precedence = models.IntegerField(default=1)

    class Meta:
        unique_together = [["job", "name"]]


class Task(models.Model):
    """ex: Scan all objects & fields (or later - scan all objects and then
    auto generate a second job with steps for every table)"""

    """ ex: load file {x} or delta load table {x}"""
    step = models.ForeignKey(Step, related_name="tasks", on_delete=CASCADE)
    name = models.CharField(max_length=250)
    object_filter = models.CharField(max_length=250, blank=True, null=True)
    source_object = models.ForeignKey(
        DataObject,
        on_delete=CASCADE,
        related_name="task_source_object",
        blank=True,
        null=True,
    )  # would be null for full meta scans
    source_type = models.ForeignKey(
        DataSourceType, on_delete=CASCADE, related_name="task_source_type"
    )  # to get the necessary image
    source_cmd = models.CharField(
        max_length=250, blank=True, null=True
    )  # python/dotnet/etc
    source_args = models.TextField(
        blank=True, null=True
    )  # scan source/object; delta load object; load deletes object; load new column object; etc;
    destination = models.ForeignKey(
        DataSource, on_delete=CASCADE, blank=True, null=True
    )
    destination_type = models.ForeignKey(
        DataSourceType,
        on_delete=CASCADE,
        blank=True,
        null=True,
        related_name="task_destination_type",
    )  # image
    destination_object = models.ForeignKey(
        DataObject,
        on_delete=CASCADE,
        blank=True,
        null=True,
        related_name="task_destination_object",
    )  # if necessary
    destination_cmd = models.CharField(max_length=250, blank=True, null=True)
    destination_args = models.TextField(
        blank=True, null=True
    )  # load raw, replicate, dv, etc

    class Meta:
        unique_together = [["step", "name"]]


class StepExecution(models.Model):
    job = models.ForeignKey(Job, on_delete=CASCADE)
    job_execution = models.ForeignKey(
        JobExecution, on_delete=CASCADE, related_name="step_executions"
    )
    start_timestamp_utc = models.DateTimeField()
    end_timestamp_utc = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=50)  # submitted, starting, running, completed
    outcome = models.CharField(max_length=50, blank=True, null=True)
    error_level = models.CharField(max_length=50, blank=True, null=True)
    error_message = models.TextField(blank=True, null=True)
    step = models.ForeignKey(Step, on_delete=CASCADE)
    precedence = models.IntegerField(default=1)

    class Meta:
        db_table = "pipeline_step_execution"


class TaskExecution(models.Model):
    step = models.ForeignKey(Step, on_delete=CASCADE)
    step_execution = models.ForeignKey(
        StepExecution, on_delete=CASCADE, related_name="task_executions"
    )
    name = models.CharField(max_length=250)
    start_timestamp_utc = models.DateTimeField(blank=True, null=True)
    end_timestamp_utc = models.DateTimeField(blank=True, null=True)
    queue_timestamp_utc = models.DateTimeField()
    reserve_timestamp_utc = models.DateTimeField(blank=True, null=True)
    pod_name = models.CharField(max_length=150, blank=True, null=True)
    status = models.CharField(max_length=50)  # submitted, starting, running, completed
    outcome = models.CharField(max_length=50, blank=True, null=True)
    error_level = models.CharField(max_length=50, blank=True, null=True)
    error_message = models.TextField(blank=True, null=True)
    task = models.ForeignKey(Task, on_delete=CASCADE)
    job = models.ForeignKey(Job, on_delete=CASCADE)
    job_execution = models.ForeignKey(JobExecution, on_delete=CASCADE)
    source_object = models.ForeignKey(
        DataObject,
        on_delete=CASCADE,
        related_name="source_object",
        blank=True,
        null=True,
    )  # would be null for full meta scans
    source_type = models.ForeignKey(
        DataSourceType, on_delete=CASCADE, related_name="source_type"
    )  # to get the necessary image
    source_cmd = models.CharField(
        max_length=250, blank=True, null=True
    )  # python/dotnet/etc
    source_args = models.TextField(
        blank=True, null=True
    )  # scan source/object; delta load object; load deletes object; load new column object; etc;
    destination_type = models.ForeignKey(
        DataSourceType,
        on_delete=CASCADE,
        blank=True,
        null=True,
        related_name="destination_type",
    )  # image
    destination_object = models.ForeignKey(
        DataObject,
        on_delete=CASCADE,
        blank=True,
        null=True,
        related_name="destination_object",
    )  # if necessary
    destination_cmd = models.CharField(max_length=250, blank=True, null=True)
    destination_args = models.TextField(
        blank=True, null=True
    )  # load raw, replicate, dv, etc

    class Meta:
        db_table = "pipeline_task_execution"
