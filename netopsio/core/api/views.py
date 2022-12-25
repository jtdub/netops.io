"""Netops.io core api views."""

from core import models, tasks
from core.api import serializers
from django_celery_results.models import TaskResult
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.response import Response

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
        data = models.TaskModel(task_id=task.task_id)
        serializer = serializers.TaskSerializer(data, context={"request": request})
        return Response(serializer.data)


class TraceRouteViewSet(viewsets.ViewSet):
    """TraceRoute Viewset."""

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "host": openapi.Schema(
                    type=openapi.TYPE_STRING, description="Host to traceroute."
                ),
            },
        )
    )  # pylint: disable=no-self-use
    def create(self, request, host=None):
        """Traceroute a host."""
        host = get_ip_address(request)
        task = tasks.traceroute.delay(host=host)
        data = models.TaskModel(task_id=task.task_id)
        serializer = serializers.TaskSerializer(data, context={"request": request})
        return Response(serializer.data)


class NmapViewSet(viewsets.ViewSet):
    """Nmap Viewset."""

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
        """Nmap a host."""
        host = get_ip_address(request)
        task = tasks.nmap.delay(host=host)
        data = models.TaskModel(task_id=task.task_id)
        serializer = serializers.TaskSerializer(data, context={"request": request})
        return Response(serializer.data)


class WhoisViewSet(viewsets.ViewSet):
    """Whois Viewset."""

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "host": openapi.Schema(
                    type=openapi.TYPE_STRING, description="Whois a domain or host."
                ),
            },
        )
    )  # pylint: disable=no-self-use
    def create(self, request, host):
        """whois a host."""
        task = tasks.whois.delay(host=host)
        data = models.TaskModel(task_id=task.task_id)
        serializer = serializers.TaskSerializer(data, context={"request": request})
        return Response(serializer.data)
