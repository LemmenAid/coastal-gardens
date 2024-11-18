from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """
    Admin configuration for the dashboard model.
    This class customizes the admin interface for the Dashboard model.
    """
    list_display = ('user',)
    search_fields = ('user__username',)
    filter_horizontal = ('saved_posts',)
