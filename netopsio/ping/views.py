"""Ping app views."""
from django.http import HttpResponse
from ping.tasks import ping


def index(request):
    if "HTTP_X_FORWARDED_FOR" in request.META:
        host = request.META["HTTP_X_FORWARDED_FOR"]
    else:
        host = request.META["REMOTE_ADDR"]
    task = ping.delay(host=host)
    return HttpResponse(f"Ping request for: {host}, Status: {task.status}")
