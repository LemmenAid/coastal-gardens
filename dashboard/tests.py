from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from blog.models import Post
from dashboard.models import UserProfile


# ------------ MODELS TESTING ------------
class UserProfileModelTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="password")
        self.post = Post.objects.create(
            title="Test Post",
            content="Content of the test post",
            author=self.user,
            status=1,
        )
        self.user_profile = self.user.profile

    def test_user_profile_created_on_user_creation(self):
        # Test that the UserProfile is created automatically
        self.assertIsNotNone(self.user_profile)
        self.assertEqual(self.user_profile.user, self.user)

    def test_save_posts_functionality(self):
        # Test saving a post to a user's profile
        self.user_profile.saved_posts.add(self.post)
        self.assertIn(self.post, self.user_profile.saved_posts.all())

        # Test removing the post
        self.user_profile.saved_posts.remove(self.post)
        self.assertNotIn(self.post, self.user_profile.saved_posts.all())


# ------------ SIGNALS TESTING ------------
class UserProfileSignalTests(TestCase):

    def test_user_profile_signal_creates_profile(self):
        user = User.objects.create_user(
            username="signaltestuser", password="password")
        self.assertTrue(UserProfile.objects.filter(user=user).exists())

    def test_user_profile_signal_saves_profile(self):
        user = User.objects.create_user(
            username="saveprofiletest", password="password")
        user.profile.garden_zone = "8a"
        user.save()
        self.assertEqual(user.profile.garden_zone, "8a")


# ------------ USER_DASHBOARD VIEW TESTING ------------
class DashboardViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="dashboarduser", password="password")
        self.client.login(username="dashboarduser", password="password")

    def test_dashboard_view(self):
        response = self.client.get(reverse("dashboard"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "dashboard/dashboard.html")
        self.assertContains(response, "Welcome")


# ------------ SAVE_POST VIEW TESTING ------------
class SavePostViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="savepostuser", password="password")
        self.post = Post.objects.create(
            title="Test Post",
            content="Test content",
            author=self.user,
            status=1,
        )
        self.client.login(username="savepostuser", password="password")

    def test_save_post_adds_to_saved_posts(self):
        response = self.client.post(reverse(
            "save_post", args=[self.post.id]))
        self.assertRedirects(response, reverse(
            "post_detail", kwargs={"slug": self.post.slug}))
        self.assertIn(self.post, self.user.profile.saved_posts.all())

    def test_save_post_removes_from_saved_posts(self):
        self.user.profile.saved_posts.add(self.post)
        response = self.client.post(reverse("save_post", args=[self.post.id]))
        self.assertRedirects(response, reverse(
            "post_detail", kwargs={"slug": self.post.slug}))
        self.assertNotIn(self.post, self.user.profile.saved_posts.all())


# ------------ CREATE MEMBER STORY VIEW TESTING ------------
class CreateMemberStoryViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="storyuser", password="password")
        self.client.login(username="storyuser", password="password")

    def test_create_member_story_get_request(self):
        response = self.client.get(reverse("create_member_story"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "dashboard/create_member_story.html")
        self.assertContains(response, "Create a Member Story")

    def test_create_member_story_post_valid_form(self):
        data = {
            "title": "Test Story",
            "content": "This is the content of the story.",
            "excerpt": "Short excerpt",
        }
        response = self.client.post(reverse("create_member_story"), data)
        self.assertRedirects(response, reverse("member_stories"))
        self.assertTrue(Post.objects.filter(title="Test Story").exists())

    def test_create_member_story_post_invalid_form(self):
        data = {"title": ""}  # Missing required fields
        response = self.client.post(reverse("create_member_story"), data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Error uploading story!")


# ------------ EDGE CASES TESTING ------------
class NonAuthenticatedAccessTests(TestCase):

    def test_dashboard_redirects_unauthenticated_user(self):
        response = self.client.get(reverse("dashboard"))
        self.assertRedirects(response, f"{reverse(
            'account_login')}?next={reverse('dashboard')}")

    def test_create_member_story_redirects_unauthenticated_user(self):
        response = self.client.get(reverse("create_member_story"))
        self.assertRedirects(response, f"{reverse(
            'account_login')}?next={reverse('create_member_story')}")
