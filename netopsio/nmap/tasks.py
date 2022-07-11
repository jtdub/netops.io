"""Celery Background Tasks"""
import subprocess
from celery import shared_task
from nmap.models import NmapRequest


@shared_task
def nmap(host: str) -> str:
    """Nmap host worker."""
    task = subprocess.run(["nmap", "-v", "-A", host], capture_output=True, check=True)
    data = NmapRequest(ip=host, result=task.stdout.decode("utf-8"))
    data.save()
    return task.stdout.decode("utf-8")
