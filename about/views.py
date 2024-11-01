from django.shortcuts import render
from .models import About

from django.http import HttpResponse
# Create your views here.

def about_me(request):
    """
    Renders the About page
    """
    about = About.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "about/about.html",
        {"about": about},
    )

def zone_map_view(request):
    return HttpResponse("Zone Map page is under construction")

def get_started_view(request):
    return HttpResponse("Get Started page is under construction")