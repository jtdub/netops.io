"Core app tests."
from core.models import RequestLog
from django.test import TestCase


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
