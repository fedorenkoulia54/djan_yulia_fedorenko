from django.test import SimpleTestCase
from django.urls import reverse

class PageTests(SimpleTestCase):

    # ✅ Позитивні
    def test_home_status(self):
        self.assertEqual(self.client.get(reverse("home")).status_code, 200)

    def test_about_status(self):
        self.assertEqual(self.client.get(reverse("about")).status_code, 200)

    def test_text_status(self):
        self.assertEqual(self.client.get(reverse("text")).status_code, 200)

    def test_resume_status(self):
        self.assertEqual(self.client.get(reverse("resume")).status_code, 200)

    def test_home_content(self):
        self.assertContains(self.client.get(reverse("home")), "Початкова сторінка")

    def test_resume_content(self):
        self.assertContains(self.client.get(reverse("resume")), "Федоренко Юлія")

 