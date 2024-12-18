from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.

from .models import Post


class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user
        testuser1 = User.objects.create(username="testuser1", password="test")
        testuser1.save()

        # Create a blog post

        test_post = Post.objects.create(
            author=testuser1, title="Blog Title", body="Blog COntents..."
        )
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f"{post.author}"
        title = f"{post.title}"
        body = f"{post.body}"

        self.assertEqual(author, "testuser1")
        self.assertEqual(title, "Blog Title")
        self.assertEqual(body, "Blog COntents...")
