"Ping app urls."
from django.urls import path
from . import views

app_name = "ping"  # pylint: disable=invalid-name
urlpatterns = [
    path("", views.index, name="ping-index"),
]
