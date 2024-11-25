from django.views import generic
from django.shortcuts import render


def handler400(request, exception):
    """Return custom 400 template"""
    return render(request, "errors/400.html", status=400)


def handler403(request, exception):
    """Return custom 403 template"""
    return render(request, "errors/403.html", status=403)


def handler404(request, exception):
    """Return custom 404 template"""
    return render(request, "errors/404.html", status=404)


def handler500(request):
    """Return custom 500 template"""
    return render(request, "errors/500.html", status=500)
