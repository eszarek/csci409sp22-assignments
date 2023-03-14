from django.db import models
from django.utils import timezone
from airports.models import Airport


# Create your models here.
class Airline(models.Model):
    airline_name = models.CharField(max_length=20)
    airline_code = models.CharField(max_length=2)


class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.PROTECT, related_name="flight_origin")
    destination = models.ForeignKey(Airport, on_delete=models.PROTECT, related_name="flight_destination")
    departure = models.DateTimeField(default=timezone.now)
    arrival = models.DateTimeField(default=timezone.now)
    aircraft_type = models.CharField(max_length=10)
    airline = models.ForeignKey(Airline, on_delete=models.PROTECT)
    flight_number = models.IntegerField()
