"""Netops.io core api urls."""

from rest_framework.routers import DefaultRouter
from core.api.views import TaskResultViewSet


router = DefaultRouter()
router.register(r"tasks", TaskResultViewSet)
