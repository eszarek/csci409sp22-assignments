from django.http import HttpResponse
from .models import Airport
from django.shortcuts import render


def index(request):
    airports = Airport.objects.all()
    context= {'airports' : airports}
    return render(request, 'airports/index.html', context)
    #airport_list = ', '.join([a.airport_code for a in airports])
    #return HttpResponse('Showing all airports: ' + airport_list);


# Create your views here.
def airport_info(request, airport_code):
    airport = Airport.objects.get(airport_code=airport_code)
    context = {'airport': airport}
    return render(request, 'airports/airport.html', context)
    #airport = Airport.objects.get(airport_code=airport_code)
    #return HttpResponse('Showing info for airport: ' + airport.name + '- ' + airport.airport_code)
