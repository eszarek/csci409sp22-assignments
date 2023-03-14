from django.db import models
from flights.models import Flight


# Create your models here.
class Reservation(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.PROTECT)
    num_people = models.IntegerField(default=1)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)


class Tickets(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.PROTECT)
    seat = models.CharField(max_length=10)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    First_Class = 'F'
    Business_Class = 'B'
    Main_Cabin = 'M'
    tickets_class_choices = [
        (First_Class, 'F'),
        (Business_Class, 'B'),
        (Main_Cabin, 'M'),
    ]
    ticket_class = models.CharField(
        max_length=1,
        choices=tickets_class_choices,
        default=Main_Cabin,
    )
