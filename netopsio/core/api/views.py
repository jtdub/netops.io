"""Netops.io core api views."""

from django_celery_results.models import TaskResult
from rest_framework import viewsets
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from core.api import serializers
from core import models, tasks
from netopsio.utilities import get_ip_address


class TaskResultViewSet(viewsets.ReadOnlyModelViewSet):
    """Rest API View for 'list' and 'retrieving' TaskResult actions."""

    queryset = TaskResult.objects.all()
    serializer_class = serializers.TaskResultSerializer
    lookup_field = "task_id"


class RequestLogViewSet(viewsets.ReadOnlyModelViewSet):
    """Rest API View for 'list' and 'retrieving' RequestLog actions."""

    queryset = models.RequestLog.objects.all()
    serializer_class = serializers.RequestLogSerializer


class PingViewSet(viewsets.ViewSet):
    """Ping Viewset."""

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "host": openapi.Schema(
                    type=openapi.TYPE_STRING, description="Host to ping."
                ),
            },
        )
    )  # pylint: disable=no-self-use
    def create(self, request, host=None):
        """Ping a host."""
        host = get_ip_address(request)
        task = tasks.ping.delay(host=host)
        data = models.Ping(task_id=task.task_id)
        serializer = serializers.TaskSerializer(data, context={"request": request})
        return Response(serializer.data)
