from django.shortcuts import render
from django.core.exceptions import BadRequest
from django.http import HttpResponseServerError


#Testing the error pages
def test_error(request):
    #return HttpResponse(status=500) #test 500 error
    raise BadRequest #test 400 error


def bad_request(request, exception):
    return render(request, '400.html', status=400)


def permission_denied(request, exception):
    return render(request, '403.html', status=403)


def page_not_found(request, exception):
    return render(request, '404.html', status=404)


def server_error(request):
    return render(request, '500.html', status=500)
