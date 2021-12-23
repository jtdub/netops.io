"""Home App and Worker Serializers."""
from rest_framework import serializers
from django_celery_results.models import TaskResult


class TaskResultSerializer(serializers.ModelSerializer):
    """TaskResult Serializer."""

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
