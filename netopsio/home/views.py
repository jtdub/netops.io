"Home app views."
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404
from django_celery_results.models import TaskResult
from rest_framework import viewsets
from home.serializers import TaskResultSerializer


def index(request):
    """Render Home Page."""
    template = loader.get_template("home/base.html")
    context = {"title": "Home"}
    return HttpResponse(template.render(context, request))


def tasks(request):
    """Render Task Results."""
    task_results = TaskResult.objects.all()
    template = loader.get_template("home/tasks.html")
    context = {"title": "Task Results", "results": task_results}
    return HttpResponse(template.render(context, request))


def task_details(request, task_id):
    """Render Task Detail Results."""
    job = get_object_or_404(TaskResult, task_id=task_id)
    result = "\n".join(job.result.strip("\"").split("\\n"))
    template = loader.get_template("home/task_details.html")
    context = {"title": "Task Details", "job": job, "result": result}
    return HttpResponse(template.render(context, request))


class TaskResultViewSet(viewsets.ReadOnlyModelViewSet):
    """Rest API View for 'list' and 'retrieving' TaskResult actions."""

    queryset = TaskResult.objects.all()
    serializer_class = TaskResultSerializer
    lookup_field = "task_id"
