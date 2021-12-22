"""Celery Background Tasks"""
import subprocess
from celery import shared_task
from ping.models import PingRequest


@shared_task
def ping(host: str, count: int = 2) -> str:
    """Ping host worker."""
    task = subprocess.run(
        ["ping", f"-c {count}", host], capture_output=True, check=True
    )
    data = PingRequest(ip=host, result=task.stdout.decode("utf-8"))
    data.save()
    return task.stdout.decode("utf-8")
