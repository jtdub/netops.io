"Ping app urls."
from django.urls import path
from traceroute import views

urlpatterns = [
    path("", views.index, name="traceroute-index"),
]
