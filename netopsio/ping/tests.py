"""Ping App Tests."""
from django.test import TestCase
from ping.models import PingRequest


class TestPing(TestCase):
    """Ping App TestCases."""

    def setUp(self):
        """Setup tests."""
        PingRequest.objects.create(ip="1.1.1.1", result="OK")

    def test_ping_models(self):
        """Test Ping App models."""
        req = PingRequest.objects.get(ip="1.1.1.1")
        self.assertEqual(req.ip, "1.1.1.1")
