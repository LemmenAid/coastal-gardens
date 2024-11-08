from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Admin configuration for the Post model, enabling a customized admin interface.

    Attributes:
    - `list_display`: Displays the title, slug, status, and creation date in the admin list view.
    - `search_fields`: Allows admin to search by title or content.
    - `list_filter`: Filters posts by status and creation date.
    - `prepopulated_fields`: Auto-populates the slug field based on the title.
    - `summernote_fields`: Enables the Summernote editor for the content field.
    """
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Comment model, providing management for comment moderation.

    Attributes:
    - `list_display`: Shows approval status, author, body, related post, and creation date in list view.
    - `list_filter`: Adds filters for approval status and creation date.
    - `search_fields`: Allows searching by author and body fields.
    - `actions`: Includes a custom action to bulk-approve selected comments.

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