"""Ping App Models."""

from django.db import models


class PingRequest(models.Model):
    """Ping Requests Logging Model."""

    date = models.DateTimeField(auto_now_add=True)
    task_id = models.UUIDField(unique=True, null=True)
    ip = models.CharField(max_length=255)
    result = models.TextField()


class Ping:
    """Ping Model."""

    def __init__(self, task_id: str):
        """Initialize the model."""
        self.task_id = task_id
