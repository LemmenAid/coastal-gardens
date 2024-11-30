from django.test import TestCase
from django.urls import reverse
from .models import About
from django.contrib.auth import get_user_model

class AboutViewTests(TestCase):

    def setUp(self):
        # Create a user and About instance for testing
        self.user = get_user_model().objects.create_user(username='testuser', password='password')
        self.about = About.objects.create(
            title="About Us",
            content="This is the content for the about page.",
            profile_image="image.jpg"
        )

    def test_about_me_view(self):
        # Test that the About page renders correctly
        response = self.client.get(reverse('about'))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about/about.html')  # Ensure the correct template is used
        self.assertContains(response, self.about.title)  # Ensure the title is included in the response
        self.assertContains(response, self.about.content)  # Ensure the content is included

    def test_about_me_view_no_about(self):
        # Ensure no About object exists
        About.objects.all().delete()

        response = self.client.get(reverse('about'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about/about.html')  # The page should still render
        self.assertContains(response, "No about content available")  # Ensure a fallback message or handling

    def test_zone_map_view(self):
        response = self.client.get(reverse('zone_map'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about/zone-map.html')  # Ensure the correct template is used

    def test_about_model_creation(self):
        about = About.objects.create(
            title="Our Story",
            content="This is a story about our company.",
            profile_image="image.jpg"
        )
        self.assertEqual(about.title, "Our Story")
        self.assertEqual(about.content, "This is a story about our company.")
        self.assertTrue(about.updated_on)  # The `updated_on` field should be auto-populated

    def test_about_str_method(self):
        about = About.objects.create(
            title="Our Story",
            content="This is a story about our company.",
            profile_image="image.jpg"
        )
        self.assertEqual(str(about), "Our Story")  # The __str__ method should return the title