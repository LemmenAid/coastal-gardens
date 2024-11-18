from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Admin configuration for the Post model,
    enabling a customized admin interface.
    """
    list_display = ('title', 'author', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Comment model,
    providing management for comment moderation.

    Methods:
    - `approve_comments`: Approves selected comments in the admin.
    """
    list_display = ('approved', 'author', 'body', 'post', 'created_on')
    list_filter = ('approved', 'created_on')
    search_fields = ('author', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
        self.message_user(request, f"Approved {queryset.count()} comments.")
    approve_comments.short_description = "Approve selected comments"
