# Generated by Django 4.0 on 2022-02-05 00:02

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("catalog", "0003_alter_contacttype_table_alter_dataobjecttype_table_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Job",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=250)),
                ("type", models.CharField(max_length=25)),
                ("is_enabled", models.BooleanField(default=True)),
                ("parallelism_degree", models.IntegerField(default=1)),
                ("description", models.TextField(blank=True, null=True)),
                ("status", models.CharField(default="new", max_length=25)),
                (
                    "data_source",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catalog.datasource",
                    ),
                ),
            ],
            options={
                "unique_together": {("data_source", "name")},
            },
        ),
        migrations.CreateModel(
            name="JobExecution",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("unique_name", models.CharField(max_length=150, unique=True)),
                (
                    "created_timestamp_utc",
                    models.DateTimeField(default=datetime.datetime.utcnow),
                ),
                ("start_timestamp_utc", models.DateTimeField(blank=True, null=True)),
                ("end_timestamp_utc", models.DateTimeField(blank=True, null=True)),
                ("status", models.CharField(max_length=50)),
                ("outcome", models.CharField(blank=True, max_length=50, null=True)),
                ("error_level", models.CharField(blank=True, max_length=50, null=True)),
                ("error_message", models.TextField(blank=True, null=True)),
                (
                    "job",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="pipeline.job"
                    ),
                ),
            ],
            options={
                "db_table": "pipeline_job_execution",
            },
        ),
        migrations.CreateModel(
            name="Step",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=250)),
                ("precedence", models.IntegerField(default=1)),
                (
                    "job",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="steps",
                        to="pipeline.job",
                    ),
                ),
            ],
            options={
                "unique_together": {("job", "name")},
            },
        ),
        migrations.CreateModel(
            name="StepExecution",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("start_timestamp_utc", models.DateTimeField()),
                ("end_timestamp_utc", models.DateTimeField(blank=True, null=True)),
                ("status", models.CharField(max_length=50)),
                ("outcome", models.CharField(blank=True, max_length=50, null=True)),
                ("error_level", models.CharField(blank=True, max_length=50, null=True)),
                ("error_message", models.TextField(blank=True, null=True)),
                ("precedence", models.IntegerField(default=1)),
                (
                    "job",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="pipeline.job"
                    ),
                ),
                (
                    "job_execution",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="step_executions",
                        to="pipeline.jobexecution",
                    ),
                ),
                (
                    "step",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="pipeline.step"
                    ),
                ),
            ],
            options={
                "db_table": "pipeline_step_execution",
            },
        ),
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=250)),
                (
                    "object_filter",
                    models.CharField(blank=True, max_length=250, null=True),
                ),
                ("source_cmd", models.CharField(blank=True, max_length=250, null=True)),
                ("source_args", models.TextField(blank=True, null=True)),
                (
                    "destination_cmd",
                    models.CharField(blank=True, max_length=250, null=True),
                ),
                ("destination_args", models.TextField(blank=True, null=True)),
                (
                    "destination",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catalog.datasource",
                    ),
                ),
                (
                    "destination_object",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="task_destination_object",
                        to="catalog.dataobject",
                    ),
                ),
                (
                    "destination_type",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="task_destination_type",
                        to="catalog.datasourcetype",
                    ),
                ),
                (
                    "source_object",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="task_source_object",
                        to="catalog.dataobject",
                    ),
                ),
                (
                    "source_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="task_source_type",
                        to="catalog.datasourcetype",
                    ),
                ),
                (
                    "step",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tasks",
                        to="pipeline.step",
                    ),
                ),
            ],
            options={
                "unique_together": {("step", "name")},
            },
        ),
        migrations.CreateModel(
            name="TaskExecution",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=250)),
                ("start_timestamp_utc", models.DateTimeField(blank=True, null=True)),
                ("end_timestamp_utc", models.DateTimeField(blank=True, null=True)),
                ("queue_timestamp_utc", models.DateTimeField()),
                ("reserve_timestamp_utc", models.DateTimeField(blank=True, null=True)),
                ("pod_name", models.CharField(blank=True, max_length=150, null=True)),
                ("status", models.CharField(max_length=50)),
                ("outcome", models.CharField(blank=True, max_length=50, null=True)),
                ("error_level", models.CharField(blank=True, max_length=50, null=True)),
                ("error_message", models.TextField(blank=True, null=True)),
                ("source_cmd", models.CharField(blank=True, max_length=250, null=True)),
                ("source_args", models.TextField(blank=True, null=True)),
                (
                    "destination_cmd",
                    models.CharField(blank=True, max_length=250, null=True),
                ),
                ("destination_args", models.TextField(blank=True, null=True)),
                (
                    "destination_object",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="destination_object",
                        to="catalog.dataobject",
                    ),
                ),
                (
                    "destination_type",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="destination_type",
                        to="catalog.datasourcetype",
                    ),
                ),
                (
                    "job",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="pipeline.job"
                    ),
                ),
                (
                    "job_execution",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="pipeline.jobexecution",
                    ),
                ),
                (
                    "source_object",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="source_object",
                        to="catalog.dataobject",
                    ),
                ),
                (
                    "source_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="source_type",
                        to="catalog.datasourcetype",
                    ),
                ),
                (
                    "step",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="pipeline.step"
                    ),
                ),
                (
                    "step_execution",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="task_executions",
                        to="pipeline.stepexecution",
                    ),
                ),
                (
                    "task",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="pipeline.task"
                    ),
                ),
            ],
            options={
                "db_table": "pipeline_task_execution",
            },
        ),
        migrations.CreateModel(
            name="JobSchedule",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=250)),
                ("start_timestamp_utc", models.DateTimeField()),
                ("end_timestamp_utc", models.DateTimeField(blank=True, null=True)),
                ("chron_string", models.CharField(max_length=50)),
                ("is_enabled", models.BooleanField(default=True)),
                (
                    "job",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="pipeline.job"
                    ),
                ),
            ],
            options={
                "db_table": "pipeline_job_schedule",
            },
        ),
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "event_timestamp_utc",
                    models.DateTimeField(default=datetime.datetime.utcnow),
                ),
                ("level", models.CharField(max_length=50)),
                ("event_type", models.CharField(max_length=50)),
                ("message", models.TextField()),
                (
                    "job_execution",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="pipeline.jobexecution",
                    ),
                ),
            ],
        ),
    ]