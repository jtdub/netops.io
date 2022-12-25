"Core app tests."
from django.test import TestCase


class CoreViewsTest(TestCase):
    """Test the Core App views."""

    def test_index_view(self):
        """Test the core page."""
        response = self.client.get("/")
        self.assertTemplateUsed(response, "core/base.html")
        self.assertEqual(response.status_code, 200)

    def test_tasks_view(self):
        """Test the tasks view."""
        response = self.client.get("/tasks/")
        self.assertTemplateUsed(response, "core/tasks.html")
        self.assertEqual(response.status_code, 200)

    def test_task_details_view(self):
        """Test the task details view."""
        response = self.client.get("/tasks/21f58fbc-e8e5-4f72-a783-47300197e7da/")
        self.assertEqual(response.status_code, 404)

    def test_ping_view(self):
        """Test the ping view."""
        response = self.client.get("/ping/")
        self.assertTemplateUsed(response, "core/task.html")
        self.assertEqual(response.status_code, 200)

    def test_traceroute_view(self):
        """Test the traceroute view."""
        response = self.client.get("/traceroute/")
        self.assertTemplateUsed(response, "core/task.html")
        self.assertEqual(response.status_code, 200)

    def test_nmap_view(self):
        """Test the nmap view."""
        response = self.client.get("/nmap/")
        self.assertTemplateUsed(response, "core/task.html")
        self.assertEqual(response.status_code, 200)

    def test_whois_view(self):
        """Test the ping view."""
        response = self.client.get("/whois/")
        self.assertTemplateUsed(response, "core/whois.html")
        self.assertEqual(response.status_code, 200)
