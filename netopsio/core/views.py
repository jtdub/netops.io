"Core app views."
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404
from django_celery_results.models import TaskResult

from core import tasks
from netopsio.utilities import get_ip_address


def index(request):
    """Render Core Page."""
    template = loader.get_template("core/base.html")
    context = {"title": "Home"}
    return HttpResponse(template.render(context, request))


def tasks_view(request):
    """Render Task Results."""
    task_results = TaskResult.objects.all()
    template = loader.get_template("core/tasks.html")
    context = {"title": "Task Results", "results": task_results}
    return HttpResponse(template.render(context, request))


def task_details(request, task_id):
    """Render Task Detail Results."""
    job = get_object_or_404(TaskResult, task_id=task_id)
    result = "\n".join(job.result.strip('"').split("\\n"))
    template = loader.get_template("core/task_details.html")
    context = {"title": "Task Details", "job": job, "result": result}
    return HttpResponse(template.render(context, request))


def ping(request):
    """Ping view."""
    host = get_ip_address(request)
    task = tasks.ping.delay(host=host)
    template = loader.get_template("core/task.html")
    context = {"host": host, "status": task.status, "id": task, "title": "Ping"}
    return HttpResponse(template.render(context, request))


def traceroute(request):
    """TraceRoute view."""
    host = get_ip_address(request)
    task = tasks.traceroute.delay(host=host)
    template = loader.get_template("core/task.html")
    context = {"host": host, "status": task.status, "id": task, "title": "Traceroute"}
    return HttpResponse(template.render(context, request))


def nmap(request):
    """Nmap view."""
    host = get_ip_address(request)
    task = tasks.nmap.delay(host=host)
    template = loader.get_template("core/task.html")
    context = {"host": host, "status": task.status, "id": task, "title": "Nmap"}
    return HttpResponse(template.render(context, request))
