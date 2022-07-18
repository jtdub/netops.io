"""Netops.io core api urls."""

from rest_framework.routers import DefaultRouter
from core.api import views


router = DefaultRouter()
router.register(r"tasks", views.TaskResultViewSet)
router.register(r"request-logs", views.RequestLogViewSet, basename="requestlog")
router.register(r"ping", views.PingViewSet, basename="ping")
router.register(r"traceroute", views.TraceRouteViewSet, basename="traceroute")
router.register(f"nmap", views.NmapViewSet, basename="nmap")
