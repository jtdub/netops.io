"""Home App and Worker Serializers."""
from rest_framework import serializers
from django_celery_results.models import TaskResult


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
