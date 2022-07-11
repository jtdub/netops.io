"""Ping app views."""
from django.http import HttpResponse
from django.template import loader
from traceroute.tasks import traceroute
from traceroute.models import TraceRouteRequest, TraceRoute
from traceroute.serializers import TraceRouteRequestSerializer, TraceRouteSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from netopsio.utilities import get_ip_address


def index(request):
    """TraceRoute app index view."""
    host = get_ip_address(request)
    task = traceroute.delay(host=host)
    template = loader.get_template("traceroute/base.html")
    context = {"host": host, "status": task.status, "id": task, "title": "Traceroute"}
    return HttpResponse(template.render(context, request))


class TraceRouteRequestViewSet(viewsets.ReadOnlyModelViewSet):
    """Rest API View for 'list' and 'retrieving' TraceRouteRequest actions."""

    queryset = TraceRouteRequest.objects.all()
    serializer_class = TraceRouteRequestSerializer


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
        task = traceroute.delay(host=host)
        data = TraceRoute(task_id=task.task_id)
        serializer = TraceRouteSerializer(data, context={"request": request})
        return Response(serializer.data)
