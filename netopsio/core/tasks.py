"""Celery Background Tasks"""
import subprocess
from celery import shared_task
from core.models import RequestLog


@shared_task
def ping(host: str, count: int = 2) -> str:
    """Ping host worker."""
    task = subprocess.run(
        ["ping", f"-c {count}", host], capture_output=True, check=True
    )
    data = RequestLog(ip=host, result=task.stdout.decode("utf-8"), app="ping")
    data.save()
    return task.stdout.decode("utf-8")
