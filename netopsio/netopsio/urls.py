"""netopsio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter
from home.views import TaskResultViewSet
from ping.views import PingRequestViewSet, PingViewSet


router = DefaultRouter()
router.register(r"tasks", TaskResultViewSet)
router.register(r"ping-logs", PingRequestViewSet)
router.register(r"ping", PingViewSet, basename="ping")


urlpatterns = [
    path("", include("home.urls"), name="home"),
    path("ping/", include("ping.urls"), name="ping"),
    path("admin/", admin.site.urls, name="admin"),
    path("api/v1/", include(router.urls), name="admin-v1"),
]
