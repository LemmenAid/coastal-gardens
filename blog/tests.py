from django.test import TestCase, Client
from django.urls import reverse
from .models import Post, Comment
from django.contrib.auth.models import User


# ------------ MODEL TESTING ------------
class BlogModelTests(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="password123")
        
        # Create a test post
        self.post = Post.objects.create(
            title="Test Post",
            content="This is a test post.",
            author=self.user,
            status=1,
            slug="test-post",
        )

    def test_post_creation(self):
        """Test that a Post is created successfully."""
        self.assertEqual(self.post.title, "Test Post")
        self.assertEqual(self.post.slug, "test-post")

    def test_comment_creation(self):
        """Test that a Comment can be created successfully."""
        comment = Comment.objects.create(
            post=self.post, author=self.user, body="This is a comment."
        )
        self.assertEqual(comment.post, self.post)
        self.assertEqual(comment.body, "This is a comment.")


# ------------ VIEWS TESTING ------------
class BlogViewTests(TestCase):
    def setUp(self):
        # Create a test user and log them in
        self.user = User.objects.create_user(username="testuser", password="password123")
        # Create another user for testing different author permissions
        self.other_user = User.objects.create_user(username='otheruser', password='password')
        self.client = Client()
        self.client.login(username="testuser", password="password123")

        # Create a test post
        self.post = Post.objects.create(
            title="Test Post",
            content="This is a test post.",
            author=self.user,
            status=1,
            slug="test-post",
        )

    # ------------ HOME PAGE TESTING ------------
    def test_home_page(self):
        """Test that the homepage loads successfully."""
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/index.html")


    # ------------ FEATURES PAGE TESTING ------------
    def test_features_page(self):
        """Test that the features page loads successfully."""
        response = self.client.get(reverse("features"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post.title)

    # ------------ MEMBER STORIES ACCESS TESTING ------------
    


    # ------------ POST_DETAIL PAGE TESTING ------------
    def test_post_detail(self):
        """Test that the post detail page loads successfully."""
        response = self.client.get(reverse("post_detail", kwargs={"slug": self.post.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post.title)
        self.assertTemplateUsed(response, "blog/post_detail.html")


    # ------------ COMMENTS TESTING ------------
    def test_add_comment(self):
        """Test that a logged-in user can add a comment."""
        response = self.client.post(
            reverse("post_detail", kwargs={"slug": self.post.slug}),
            {"body": "This is a test comment."},
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Comment.objects.filter(body="This is a test comment.").exists())


    def test_edit_comment(self):
        """Test that a user can edit their comment."""
        comment = Comment.objects.create(post=self.post, author=self.user, body="Original content")
        response = self.client.post(
            reverse("comment_edit", kwargs={"slug": self.post.slug, "comment_id": comment.id}),
            {"body": "Edited content"},
        )
        comment.refresh_from_db()
        self.assertEqual(comment.body, "Edited content")


    def test_delete_comment(self):
        """Test that a user can delete their comment."""
        comment = Comment.objects.create(post=self.post, author=self.user, body="To be deleted")
        response = self.client.post(
            reverse("comment_delete", kwargs={"slug": self.post.slug, "comment_id": comment.id})
        )
        self.assertFalse(Comment.objects.filter(body="To be deleted").exists())


    def test_comment_delete_unauthorized(self):
        comment = Comment.objects.create(
            post=self.post,
            author=self.other_user,  # Different user
            body="Unauthorized delete test"
        )
        response = self.client.post(reverse('comment_delete', args=[self.post.slug, comment.id]))
        self.assertEqual(Comment.objects.filter(id=comment.id).count(), 1)
        self.assertRedirects(response, reverse('post_detail', args=[self.post.slug]))
