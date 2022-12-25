"Core app views."
from core import forms, tasks
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template import loader
from django_celery_results.models import TaskResult

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


def whois(request):
    """Whois view."""
    if request.method == "POST":
        form = forms.WhoisForm(request.POST)

        if form.is_valid():
            host = form.cleaned_data["host"]
            task = tasks.whois.delay(host)
            template = loader.get_template("core/task.html")
            context = {
                "host": host,
                "status": task.status,
                "id": task,
                "title": "Whois",
            }
            return HttpResponse(template.render(context, request))

    else:
        context = {"form": forms.WhoisForm(), "title": "Whois"}
        template = loader.get_template("core/whois.html")
        return HttpResponse(template.render(context, request))
