from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello from Airports')


# Create your views here.
def airport_info(request, airport_code):
    return HttpResponse("Showing info for airport: " + airport_code)
