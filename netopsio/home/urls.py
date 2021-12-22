"Home app urls."
from django.urls import path
from . import views

app_name = ""  # pylint: disable=invalid-name
urlpatterns = [
    path("", views.index, name="home_index"),
    path("results/", views.results, name="home_results"),
    path("results/<str:task_id>/", views.result_details, name="results_details"),
]
