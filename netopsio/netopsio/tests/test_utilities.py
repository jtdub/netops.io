"""Test netopsio utilities."""
from django.test import RequestFactory, TestCase

from netopsio import utilities


class UtilitiesTestCase(TestCase):
    """Test Utilities."""

    def setUp(self):
        """Setup tests."""
        self.request = RequestFactory()

    def test_get_ip_address(self):
        """Test get_ip_address."""
        response = self.request.get("/")
        self.assertEqual(utilities.get_ip_address(response), "127.0.0.1")

        response.META["HTTP_X_FORWARDED_FOR"] = response.META["REMOTE_ADDR"]
        self.assertEqual(utilities.get_ip_address(response), "127.0.0.1")
