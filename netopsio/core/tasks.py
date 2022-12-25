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


@shared_task
def traceroute(host: str) -> str:
    """Traceroute host worker."""
    task = subprocess.run(["traceroute", host], capture_output=True, check=True)
    data = RequestLog(ip=host, result=task.stdout.decode("utf-8"), app="traceroute")
    data.save()
    return task.stdout.decode("utf-8")


@shared_task
def nmap(host: str) -> str:
    """Nmap host worker."""
    task = subprocess.run(["nmap", "-v", "-A", host], capture_output=True, check=True)
    data = RequestLog(ip=host, result=task.stdout.decode("utf-8"), app="nmap")
    data.save()
    return task.stdout.decode("utf-8")


@shared_task
def whois(host: str) -> str:
    """Whois host worker."""
    task = subprocess.run(["whois", host], capture_output=True, check=True)
    data = RequestLog(ip=host, result=task.stdout.decode("utf-8"), app="whois")
    data.save()
    return task.stdout.decode("utf-8")
