from django.shortcuts import render, redirect
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
    - ``user``: The current authenticated user instance.
    - ``user_posts``: Posts or data specific to the user.

    **Template**
    :template:`dashboard.html`
    """
    user_profile = request.user.profile
    user_posts = Post.objects.filter(author=request.user)
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
    post = Post.objects.get(id=post_id)
    if post in request.user.profile.saved_posts.all():
        request.user.profile.saved_posts.remove(post)
    else:
        request.user.profile.saved_posts.add(post)
    return redirect("post_detail", slug=post.slug)


@login_required
def create_member_story(request):
    if request.method == "POST":
        form = MemberStoryForm(request.POST, request.FILES)
        if form.is_valid():
            story = form.save(commit=False)
            story.author = request.user
            story.is_member_story = True
            story.status = 1  # Set status to published
            story.save()
            return redirect("member_stories")
    else:
        form = MemberStoryForm()
    return render(request, "dashboard/create_member_story.html", {"form": form})
