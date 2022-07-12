"Core app urls."
from django.urls import path
from core import views

app_name = ""  # pylint: disable=invalid-name
urlpatterns = [
    path("", views.index, name="core-index"),
    path("tasks/", views.tasks, name="tasks"),
    path("tasks/<str:task_id>/", views.task_details, name="task-details"),
]
