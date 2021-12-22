"Home app urls."
from django.urls import path
from . import views

app_name = ""  # pylint: disable=invalid-name
urlpatterns = [
    path("", views.index, name="home-index"),
    path("results/", views.results, name="results"),
    path("results/<str:task_id>/", views.result_details, name="result-details"),
]
