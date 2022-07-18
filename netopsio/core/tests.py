"Core app tests."
from django.test import TestCase
from core.models import RequestLog


class CoreViewsTest(TestCase):
    """Test the Core App views."""

    def test_index_view(self):
        """Test the core page."""
        response = self.client.get("/")
        self.assertTemplateUsed(response, "core/base.html")
        self.assertEqual(response.status_code, 200)


class RequestLogTestCase(TestCase):
    """RequestLog TestCases."""

    def setUp(self):
        """Setup tests."""
        RequestLog.objects.create(ip="1.1.1.1", result="OK", app="ping")
        return super().setUp()

    def test_requestlog_models(self):
        """Test RequestLog models."""
        req = RequestLog.objects.get(ip="1.1.1.1")
        self.assertEqual(req.ip, "1.1.1.1")
