"""Ping app views."""
from django.http import HttpResponse
from django.template import loader
from nmap.tasks import nmap
from nmap.models import NmapRequest, Nmap
from nmap.serializers import NmapRequestSerializer, NmapSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from netopsio.utilities import get_ip_address


def index(request):
    """Nmap app index view."""
    host = get_ip_address(request)
    task = nmap.delay(host=host)
    template = loader.get_template("nmap/base.html")
    context = {"host": host, "status": task.status, "id": task, "title": "Nmap"}
    return HttpResponse(template.render(context, request))


class NmapRequestViewSet(viewsets.ReadOnlyModelViewSet):
    """Rest API View for 'list' and 'retrieving' NmapRequest actions."""

    queryset = NmapRequest.objects.all()
    serializer_class = NmapRequestSerializer


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
        task = nmap.delay(host=host)
        data = Nmap(task_id=task.task_id)
        serializer = NmapSerializer(data, context={"request": request})
        return Response(serializer.data)
