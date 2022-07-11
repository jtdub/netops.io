"""Ping App Tests."""
from django.test import TestCase
from traceroute.models import TraceRouteRequest


class TestTraceRoute(TestCase):
    """TraceRoute App TestCases."""

    def setUp(self):
        """Setup tests."""
        TraceRouteRequest.objects.create(ip="1.1.1.1", result="OK")

    def test_traceroute_models(self):
        """Test TraceRoute App models."""
        req = TraceRouteRequest.objects.get(ip="1.1.1.1")
        self.assertEqual(req.ip, "1.1.1.1")
