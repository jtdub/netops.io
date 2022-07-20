"""Core tasks tests."""


from django.test import TestCase

from core import tasks


class TasksTestCase(TestCase):
    def setUp(self):
        self.host = "localhost"

    def test_ping_task(self):
        ping = tasks.ping.delay(host=self.host)
        self.assertIn(ping.status, ("PENDING", "STARTED", "SUCCESS"))

    def test_traceroute_task(self):
        traceroute = tasks.ping.delay(host=self.host)
        self.assertIn(traceroute.status, ("PENDING", "STARTED", "SUCCESS"))

    def test_nmap_task(self):
        nmap = tasks.nmap.delay(host=self.host)
        self.assertIn(nmap.status, ("PENDING", "STARTED", "SUCCESS"))
