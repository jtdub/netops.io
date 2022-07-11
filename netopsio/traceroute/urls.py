"Ping app urls."
from django.urls import path
from traceroute import views

app_name = ""
urlpatterns = [
    path("", views.index, name="traceroute-index"),
]
