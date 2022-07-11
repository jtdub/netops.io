"""Celery Background Tasks"""
import subprocess
from celery import shared_task
from traceroute.models import TraceRouteRequest


@shared_task
def traceroute(host: str, count: int = 2) -> str:
    """Traceroute host worker."""
    task = subprocess.run(["traceroute", host], capture_output=True, check=True)
    data = TraceRouteRequest(ip=host, result=task.stdout.decode("utf-8"))
    data.save()
    return task.stdout.decode("utf-8")
