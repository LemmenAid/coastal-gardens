from django.shortcuts import render
from django.http import HttpResponse
from .models import About


def about_me(request):
    """
    Renders the About page with the most recent content.
    Displays an individual instance of :model:`about.About`.

    **Context**
    ``about``
        The most recent instance of :model:`about.About`.

    **Template:**
    :template:`about/about.html`
    """
    about = About.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "about/about.html",
        {"about": about},
    )


def zone_map_view(request):
    """
    Renders the Zone Map page.

    **Template:**
    :template:`about/zone-map.html`
    """
    return render(request, 'about/zone-map.html')


def get_started_view(request):
    """
    """
    return HttpResponse("Get Started page is under construction")
