from django.test import TestCase


class HomeViewsTest(TestCase):
    """Test the Home App views."""

    def test_index_view(self):
        """Test the home page."""
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home/base.html")
        self.assertEqual(response.status_code, 200)
