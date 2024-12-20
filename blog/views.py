from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm


def home(request):
    """
    Renders the homepage for the blog.

    **Template:**
    :template:`blog/index.html`
    """
    latest_posts = Post.objects.filter(status=1,
                                       is_member_story=False).order_by(
                                       "-created_on")[:3]
    return render(request, 'blog/index.html', {'latest_posts': latest_posts})


class PostList(generic.ListView):
    """
    Displays a list of published blog posts.

    **Context**
    ``object_list``
        A list of published posts, ordered by creation date.

    **Template:**
    :template:`blog/features.html`
    """
    queryset = Post.objects.filter(status=1,
                                   is_member_story=False).order_by(
                                   "-created_on")
    template_name = "blog/features.html"
    paginate_by = 3


class MemberStoriesView(LoginRequiredMixin, generic.ListView):
    """
    Displays a paginated list of member stories posts.

    **Context**
    ``object_list``
        A list of published stories by members, ordered by creation date.

    **Template:**
    :template:`blog/member_stories.html`
    """
    queryset = Post.objects.filter(status=1,
                                   is_member_story=True).order_by(
                                   "-created_on")
    template_name = "blog/member_stories.html"
    context_object_name = "stories"
    paginate_by = 3


def post_detail(request, slug):
    """
    Displays an individual blog post along with its comments.

    **Context**
    ``post``
        An instance of :model:`blog.Post`.
    ``comments``
        All approved comments related to the post.
    ``comment_count``
        The number of approved comments for the post.
    ``comment_form``
        An instance of :form:`blog.CommentForm`..

    **Template:**
    :template:`blog/post_detail.html`
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    # Restrict access if post is a member story and user is not authenticated
    if post.is_member_story and not request.user.is_authenticated:
        messages.warning(request,
                         "You must be logged in to view this member story.")
        return redirect(reverse('account_login'))

    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect(reverse('account_login'))

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    comment_form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {"post": post,
         "comments": comments,
         "comment_count": comment_count,
         "comment_form": comment_form,
         },
    )


@login_required
def comment_edit(request, slug, comment_id):
    """
    Display an individual comment for edit.

    **Context**
    ``post``
        An instance of :model:`blog.Post`.
    ``comment``
        All approved comments related to the post.
    ``comment_form``
        An instance of :form:`blog.CommentForm`..
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


@login_required
def comment_delete(request, slug, comment_id):
    """
    Delete an individual comment from a blog post.

    ``post``
        An instance of :model:`blog.Post`.
    ``comment``
        All approved comments related to the post.
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own comments!')
    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


@login_required
def delete_story(request, slug):
    """
    Allows the author to delete their story.
    """
    post = get_object_or_404(Post, slug=slug)

    if request.user != post.author:
        messages.error(request, "You are not authorized to delete this story.")
        return redirect('post_detail', slug=slug)

    post.delete()
    messages.success(request, "Your story has been successfully deleted.")
    return redirect('member_stories')
