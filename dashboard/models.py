from django.db import models
from django.contrib.auth.models import User
from blog.models import Post


class UserProfile(models.Model):
    """
    A model to manage user-specific data related to gardening
    and blog interactions.

    Attributes:
        user: Links to a Django User instance with a one-to-one relationship.
        garden_zone: Optional, stores the gardening zone
        (e.g., '8a', '9b') as a string.
        saved_posts: Optional, allows users to save blog posts
        for quick access.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='profile')
    garden_zone = models.CharField(max_length=20, blank=True)
    saved_posts = models.ManyToManyField(Post, blank=True,
                                         related_name="saved_by")
