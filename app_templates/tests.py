from django.test import SimpleTestCase
from django.urls import reverse

class PageTests(SimpleTestCase):

    def test_home_status_code(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_about_status_code(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)

    def test_home_template(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")

    def test_about_template(self):
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "about.html")

    def test_home_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "<h1>Початкова сторінка</h1>")

    def test_about_content(self):
        response = self.client.get(reverse("about"))
        self.assertContains(response, "<h1>Сторінка about</h1>")
