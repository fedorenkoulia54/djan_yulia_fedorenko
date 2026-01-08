from django.test import TestCase
from django.urls import reverse
from .models import Post

class BlogCrudTests(TestCase):

    def test_create_post(self):
        response = self.client.post(reverse("post_new"), {"title": "T1", "body": "B1"})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.count(), 1)

    def test_update_post(self):
        p = Post.objects.create(title="Old", body="Body")
        response = self.client.post(reverse("post_edit", args=[p.pk]), {"title": "New", "body": "Body2"})
        self.assertEqual(response.status_code, 302)
        p.refresh_from_db()
        self.assertEqual(p.title, "New")

    def test_delete_post(self):
        p = Post.objects.create(title="Del", body="Body")
        response = self.client.post(reverse("post_delete", args=[p.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.count(), 0)
