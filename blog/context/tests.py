from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Blog_Posts


class BlogPageTests(TestCase):
    def setUp(self):
        self.post = Blog_Posts.objects.create(
            title="Test post",
            content="<p>Test content</p>",
        )

    def test_root_redirects_to_blog_home(self):
        response = self.client.get("/")
        self.assertRedirects(response, "/context/")

    def test_home_page_loads(self):
        response = self.client.get(reverse("blog:index"))
        self.assertEqual(response.status_code, 200)

    def test_about_page_loads(self):
        response = self.client.get(reverse("blog:aboutme"))
        self.assertEqual(response.status_code, 200)

    def test_post_list_loads_and_shows_post(self):
        response = self.client.get(reverse("blog:list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test post")

    def test_post_detail_loads_and_sanitizes_html(self):
        self.post.content = (
            '<p onclick="alert(1)">Safe text'
            '<script>alert("xss")</script></p>'
        )
        self.post.save()

        response = self.client.get(
            reverse("blog:detail", args=[self.post.pk])
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<p>Safe text</p>", html=True)
        self.assertNotContains(response, "onclick")
        self.assertNotContains(response, "<script>")
        self.assertNotContains(response, 'alert("xss")')

    def test_published_time_uses_a_callable_default(self):
        before = timezone.now()
        post = Blog_Posts.objects.create(
            title="Default timestamp",
            content="",
        )
        after = timezone.now()

        self.assertGreaterEqual(post.published_time, before)
        self.assertLessEqual(post.published_time, after)


class BlogAdminTests(TestCase):
    def test_admin_requires_authentication(self):
        response = self.client.get(
            reverse("admin:context_blog_posts_changelist")
        )
        self.assertEqual(response.status_code, 302)
        self.assertIn("/admin/login/", response.url)

    def test_staff_user_can_open_blog_admin(self):
        Blog_Posts.objects.create(title="Admin test post", content="")
        user = get_user_model().objects.create_superuser(
            username="site-owner",
            email="owner@example.com",
            password="test-only-password",
        )
        self.client.force_login(user)

        response = self.client.get(
            reverse("admin:context_blog_posts_changelist")
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Admin test post")

    def test_non_staff_user_cannot_open_blog_admin(self):
        user = get_user_model().objects.create_user(
            username="regular-user",
            password="test-only-password",
            is_staff=False,
        )
        self.client.force_login(user)

        response = self.client.get(
            reverse("admin:context_blog_posts_changelist")
        )

        self.assertEqual(response.status_code, 302)
