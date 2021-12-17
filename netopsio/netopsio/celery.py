"""Celery Jobs Initialization"""

import os

from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "proj.settings")

app = Celery("netopsio")
app.config_from_object("django.conf:settings", namespace="NETOPSIO")
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    """Celery Debug Task"""
    print(f"Request: {self.request!r}")
