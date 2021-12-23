"Home app urls."
from django.urls import path
from . import views

app_name = ""  # pylint: disable=invalid-name
urlpatterns = [
    path("", views.index, name="home-index"),
    path("tasks/", views.tasks, name="tasks"),
    path("tasks/<str:task_id>/", views.task_details, name="task-details"),
]
