"""Core api tests."""
from core.api import views
from django.test import TestCase
from rest_framework.test import APIRequestFactory


class CoreApiTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.ping = views.PingViewSet()
        self.traceroute = views.TraceRouteViewSet()
        self.nmap = views.NmapViewSet()
        self.host = {"host": "localhost"}
        self.content_type = {"Content-type": "application/json"}
        return super().setUp()

    def test_ping_api(self):
        request = self.factory.post(
            "/api/v1/ping/",
            self.host,
            content_type=self.content_type,
        )
        response = self.ping.create(request)
        self.assertEqual(response.status_code, 200)

    def test_traceroute_api(self):
        request = self.factory.post(
            "/api/v1/traceroute/",
            self.host,
            content_type=self.content_type,
        )
        response = self.traceroute.create(request)
        self.assertEqual(response.status_code, 200)

    def test_nmap_api(self):
        request = self.factory.post(
            "/api/v1/nmap/",
            self.host,
            content_type=self.content_type,
        )
        response = self.nmap.create(request)
        self.assertEqual(response.status_code, 200)
