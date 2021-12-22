"""Ping app views."""
from django.http import HttpResponse
from django.template import loader
from ping.tasks import ping
from ping.models import PingRequest
from ping.serializers import PingRequestSerializer
from rest_framework import viewsets


def index(request):
    """Ping app index view."""
    host = request.GET.get("host")

    if host is None:
        if "HTTP_X_FORWARDED_FOR" in request.META:
            host = request.META["HTTP_X_FORWARDED_FOR"]
        else:
            host = request.META["REMOTE_ADDR"]

    task = ping.delay(host=host)
    template = loader.get_template("ping/base.html")
    context = {"host": host, "status": task.status, "id": task, "title": "Ping"}
    return HttpResponse(template.render(context, request))


class PingRequestViewSet(viewsets.ReadOnlyModelViewSet):
    """Rest API View for 'list' and 'retrieving' PingRequest actions."""

    queryset = PingRequest.objects.all()
    serializer_class = PingRequestSerializer
