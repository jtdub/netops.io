"""Nmap App Tests."""
from django.test import TestCase
from nmap.models import NmapRequest


class TestNmap(TestCase):
    """Nmap App TestCases."""

    def setUp(self):
        """Setup tests."""
        NmapRequest.objects.create(ip="1.1.1.1", result="OK")

    def test_nmap_models(self):
        """Test Nmap App models."""
        req = NmapRequest.objects.get(ip="1.1.1.1")
        self.assertEqual(req.ip, "1.1.1.1")
