from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from blog.models import Post
from .forms import MemberStoryForm
from .models import UserProfile


for user in User.objects.all():
    UserProfile.objects.get_or_create(user=user)


@login_required
def user_dashboard(request):
    """
    Renders the personalized user dashboard.

     **Context**
    - ``user_profile``: The profile of the current authenticated user.
    - ``user_posts``: Published posts authored by the user.
    - ``saved_posts``: Posts saved by the user.
    - ``user_comments``: Comments made by the user.

    **Template**
    :template:`dashboard.html`
    """
    user_profile = request.user.profile
    user_posts = Post.objects.filter(author=request.user,
                                     is_member_story=True, status=1)
    saved_posts = user_profile.saved_posts.all()
    user_comments = request.user.commenter.all()

    return render(request, "dashboard/dashboard.html", {
        "user_profile": user_profile,
        "user_posts": user_posts,
        "saved_posts": saved_posts,
        "user_comments": user_comments,
    })


@login_required
def save_post(request, post_id):
    """
    Toggles the saved state of a blog post for the logged-in user.

    If the post is already saved by the user,
    it will be removed from their saved posts.
    If it is not saved, it will be added to their saved posts.

    Args:
        request: The HTTP request object.
        post_id: The ID of the post to toggle the saved state for.

    Returns:
        Redirects to the post's detail page.
    """
    post = get_object_or_404(Post, id=post_id)

    if post in request.user.profile.saved_posts.all():
        messages.add_message(request, messages.SUCCESS,
                             'Story removed from your Dashboard.')
        request.user.profile.saved_posts.remove(post)
    else:
        messages.add_message(request, messages.SUCCESS,
                             'Story added to your Dashboard.')
        request.user.profile.saved_posts.add(post)
    return redirect("post_detail", slug=post.slug)


@login_required
def create_member_story(request):
    """
    Allows logged-in users to create and submit a new member story.

    Handles both displaying the form and processing form submissions.
    If the form submission is valid, the story is saved as authored by the user
    and marked as a member story with a published status.

    Args:
        request: The HTTP request object.

    Returns:
        - Renders the "create_member_story" template if request method is GET.
        - Redirects to "member_stories" page upon successful form submission.
    """
    if request.method == "POST":
        form = MemberStoryForm(request.POST, request.FILES)
        if form.is_valid():
            story = form.save(commit=False)
            story.author = request.user
            story.is_member_story = True
            story.status = 0  # Set status to draft
            story.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Story waiting for approval!')
            return redirect("member_stories")
    else:
        messages.add_message(request, messages.ERROR,
                             'Error uploading story!')
        form = MemberStoryForm()
    return render(request, "dashboard/create_member_story.html",
                  {"form": form})
