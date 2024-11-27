from django.urls import path
from . import views
from blog import views as blog_views


urlpatterns = [
    path("", views.user_dashboard, name="dashboard"),
    path("save-post/<int:post_id>/", views.save_post,
         name="save_post"),
    path("member-stories/", blog_views.MemberStoriesView.as_view(),
         name="member_stories"),
    path("create-story/", views.create_member_story,
         name="create_member_story"),
]
