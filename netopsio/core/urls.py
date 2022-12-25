"Core app urls."
from core import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="core-index"),
    path("tasks/", views.tasks_view, name="tasks"),
    path("tasks/<str:task_id>/", views.task_details, name="task-details"),
    path("ping/", views.ping, name="ping"),
    path("traceroute/", views.traceroute, name="traceroute"),
    path("nmap/", views.nmap, name="nmap"),
    path("whois/", views.whois, name="whois"),
]
