from django import forms


class FlightForm(forms.Form):
    origin = forms.CharField(label='origin')
    destination = forms.CharField(label='destination')
