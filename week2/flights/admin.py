from django.contrib import admin
from .models import Airline, Flight


# Register your models here.
class AirlineAdmin(admin.ModelAdmin):
    fields = ['airline_name', 'airline_code']


class FlightAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Airline Information', {'fields': ['airline', 'flight_number']}),
        ('Origin/Destination', {'fields': ['origin', 'destination']}),
        ('Departure and Arrival Time', {'fields': ['departure', 'arrival'], 'classes': ['collapse']})
    ]


admin.site.register(Airline, AirlineAdmin)
admin.site.register(Flight, FlightAdmin)
