from django.db import models
from django.contrib.auth.models import User
from blog.models import Post


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    garden_zone = models.CharField(max_length=20, blank=True)
    saved_posts = models.ManyToManyField(Post, blank=True, related_name="saved_by")
