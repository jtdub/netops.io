"""Celery Background Tasks"""
from celery import shared_task
from ping.models import PingRequest
import subprocess


@shared_task
def ping(host: str, count: int = 2) -> str:
    """Ping host worker."""
    task = subprocess.run(["ping", f"-c {count}", host], capture_output=True)
    data = PingRequest(ip=host, result=task.stdout.decode("utf-8"))
    data.save()
