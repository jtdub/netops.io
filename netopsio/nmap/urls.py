"Ping app urls."
from django.urls import path
from nmap import views

urlpatterns = [
    path("", views.index, name="nmap-index"),
]
