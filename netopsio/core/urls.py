"Core app urls."
from django.urls import path
from core import views


urlpatterns = [
    path("", views.index, name="core-index"),
    path("tasks/", views.tasks_view, name="tasks"),
    path("tasks/<str:task_id>/", views.task_details, name="task-details"),
    path("ping/", views.ping, name="ping"),
]
