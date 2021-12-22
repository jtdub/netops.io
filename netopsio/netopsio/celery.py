"""Celery Jobs Initialization"""

import os

from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "netopsio.settings")

app = Celery(
    "netopsio",
    broker=f"{os.getenv('NETOPSIO_BROKER_URL')}",
)
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    """Celery Debug Task"""
    print(f"Request: {self.request!r}")
