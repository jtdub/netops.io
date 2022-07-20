"""Core App and Worker Serializers."""
from django_celery_results.models import TaskResult
from rest_framework import serializers

from core import models


class TaskResultSerializer(serializers.HyperlinkedModelSerializer):
    """TaskResult Serializer."""

    url = serializers.HyperlinkedIdentityField(
        view_name="taskresult-detail", lookup_field="task_id"
    )

    class Meta:
        """Task Result Serializer Meta."""

        model = TaskResult
        fields = [
            "task_id",
            "task_name",
            "task_kwargs",
            "status",
            "result",
            "date_created",
            "date_done",
            "url",
        ]


class TaskSerializer(serializers.Serializer):  # pylint: disable=abstract-method
    """Ping Serializer."""

    task_id = serializers.CharField(max_length=512)


class RequestLogSerializer(serializers.ModelSerializer):
    """RequestLog Serializer."""

    class Meta:
        """RequestLog Serializer Meta."""

        model = models.RequestLog
        fields = ["id", "date", "task_id", "ip", "app", "result", "url"]
