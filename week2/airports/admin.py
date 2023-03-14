from django.contrib import admin
from .models import Airport, Runway


# Register your models here.
class RunwayInLine(admin.StackedInline):
    model = Runway  # which model to use
    extra = 2  # how many to start with


class AirportAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'airport_code', 'is_open']}),
        ('Airport Address', {'fields': ['address', 'city', 'state', 'zipcode'],
                             'classes': ['collapse']})
    ]
    inlines = [RunwayInLine]  # load the runway inline class, added the ability to add a runway


admin.site.register(Airport, AirportAdmin)
