from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post


# Create your views here.

def home(request):
    return render(request, 'blog/index.html')

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("created_on")
    template_name = "blog/features.html"
    paginate_by = 3


def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    return render(
        request,
        "blog/post_detail.html",
        {"post": post,
        "comments": comments,
        "comment_count": comment_count,
        },
    )