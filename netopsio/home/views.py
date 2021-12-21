"Home app views."
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404
from django_celery_results.models import TaskResult


def index(request):
    """Render Home Page."""
    template = loader.get_template("home/base.html")
    context = {"title": "Home"}
    return HttpResponse(template.render(context, request))


def result(request, task_id):
    """Render Task Results."""
    job = get_object_or_404(TaskResult, task_id=task_id)
    template = loader.get_template("home/result.html")
    context = {"title": "Task Result", "job": job}
    return HttpResponse(template.render(context, request))
