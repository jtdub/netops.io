"""Netops.io core app models."""

from django.db import models


class RequestLog(models.Model):
    """Request Logging Model."""

    date = models.DateTimeField(auto_now_add=True)
    task_id = models.UUIDField(unique=True, null=True)
    ip = models.CharField(max_length=255)
    result = models.TextField()
    app = models.CharField(max_length=255)


class TaskModel:
    """Task Model."""

    def __init__(self, task_id: str):
        """Initialize the model."""
        self.task_id = task_id
