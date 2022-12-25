"""Netops.io core api urls."""

from core.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"tasks", views.TaskResultViewSet)
router.register(r"request-logs", views.RequestLogViewSet, basename="requestlog")
router.register(r"ping", views.PingViewSet, basename="ping")
router.register(r"traceroute", views.TraceRouteViewSet, basename="traceroute")
router.register(r"nmap", views.NmapViewSet, basename="nmap")
router.register(r"whois", views.WhoisViewSet, basename="whois")
