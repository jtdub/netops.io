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
from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from home.views import TaskResultViewSet
from ping.views import PingRequestViewSet, PingViewSet
from traceroute.views import TraceRouteRequestViewSet, TraceRouteViewSet


router = DefaultRouter()
router.register(r"tasks", TaskResultViewSet)
router.register(r"ping-logs", PingRequestViewSet)
router.register(r"ping", PingViewSet, basename="ping")
router.register(r"traceroute-logs", TraceRouteRequestViewSet)
router.register(r"traceroute", TraceRouteViewSet, basename="traceroute")


schema_view = get_schema_view(  # pylint: disable=invalid-name
    openapi.Info(
        title="NetOps.io API",
        default_version="v1",
        description="NetOps.io API Documentation",
        license=openapi.License(name="Apache License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path("", include("home.urls"), name="home"),
    path("ping/", include("ping.urls"), name="ping"),
    path("traceroute/", include("traceroute.urls"), name="traceroute"),
    path("admin/", admin.site.urls, name="admin"),
    path("api/v1/", include(router.urls), name="admin-v1"),
    re_path(
        r"^api/docs/(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^api/docs/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
