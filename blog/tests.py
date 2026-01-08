from django.test import TestCase
from django.urls import reverse
from .models import Post

class BlogTests(TestCase):
    def test_blog_status_code(self):
        response = self.client.get("/blog/")
        self.assertEqual(response.status_code, 200)

    def test_blog_url_name(self):
        response = self.client.get(reverse("blog"))
        self.assertEqual(response.status_code, 200)

    def test_blog_template(self):
        response = self.client.get(reverse("blog"))
        self.assertTemplateUsed(response, "blog.html")

    def test_blog_content(self):
        Post.objects.create(title="Test title", body="Test body")
        response = self.client.get(reverse("blog"))
        self.assertContains(response, "Test title")
