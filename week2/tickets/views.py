from django.http import HttpResponse
from .models import Reservation
from .forms import TicketForm
from django.shortcuts import render


def index(request):
    # instance of ticket form
    form = TicketForm()

    # render form
    return render(request, 'tickets/index.html', {'form': form})


def search(request):
    form = TicketForm(request.POST)
    if form.is_valid():
        reservation = Reservation.objects.get(id=form.cleaned_data['confirmation_number'])
        return render(request, 'tickets/ticket_search.html', {'reservation': reservation})


def ticket_search(request, confirmation_number):
    # Select the singular reservation for the confirmation number
    # Note: the confirmation_number is the id in the Reservation table
    reservation = reservation = Reservation.objects.get(pk=confirmation_number)
    return HttpResponse(
        'Number of tickets for confirmation number: ' + str(confirmation_number) + " is " + str(reservation.num_people))
