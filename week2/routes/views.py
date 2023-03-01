from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello from Routes')


# Create your views here.
def route_search(request, origin, destination):
    return HttpResponse("Showing routes from " + origin + " to " + destination)
