"Core app tests."
from django.test import TestCase


class CoreViewsTest(TestCase):
    """Test the Core App views."""

    def test_index_view(self):
        """Test the core page."""
        response = self.client.get("/")
        self.assertTemplateUsed(response, "core/base.html")
        self.assertEqual(response.status_code, 200)
