from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello from Flights')
# Create your views here.
def flight_search(request, origin, destination):
    return HttpResponse("Showing flights from " + origin + " to " + destination)
