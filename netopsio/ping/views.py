"""Ping app views."""
from django.http import HttpResponse
from django.template import loader
from ping.tasks import ping
from ping.models import PingRequest, Ping
from ping.serializers import PingRequestSerializer, PingSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from netopsio.utilities import get_ip_address


def index(request):
    """Ping app index view."""
    host = get_ip_address(request)
    task = ping.delay(host=host)
    template = loader.get_template("ping/base.html")
    context = {"host": host, "status": task.status, "id": task, "title": "Ping"}
    return HttpResponse(template.render(context, request))


class PingRequestViewSet(viewsets.ReadOnlyModelViewSet):
    """Rest API View for 'list' and 'retrieving' PingRequest actions."""

    queryset = PingRequest.objects.all()
    serializer_class = PingRequestSerializer


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
        task = ping.delay(host=host)
        data = Ping(task_id=task.task_id)
        serializer = PingSerializer(data, context={"request": request})
        return Response(serializer.data)
