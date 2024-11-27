from django.shortcuts import render

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse


def home(request: WSGIRequest):
    return render(request, 'index.html')


def about(request: WSGIRequest):
    return HttpResponse("<h1>FN26 guruhi<h1>")


def contact(request):
    return HttpResponse("Contact")