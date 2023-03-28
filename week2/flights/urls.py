# Load path from django.url
from django.contrib import admin

# load this application from views.py
from django.urls import path

from . import views

# define URL pattern
urlpatterns = [
    # Get index view
    # Example url: /airports/
    path('', views.index),
    # Show Airport info
    # Example url /airports/MYR
    # NOTICE: the airport_code parameter in the url matches
    #       the parameter in the airport_info function
    path('/search/<str:origin>/<str:destination>/', views.flight_search),

    path('search/', views.search),
]
