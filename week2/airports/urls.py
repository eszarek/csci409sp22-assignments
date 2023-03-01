# Load path from django.url
from django.contrib import admin

# load this application from views.py
from django.urls import path

from . import views

# define URL pattern
urlpatterns = [
    # get index view
    # Starting with airports/
    path('', views.index),

    # Show import info by code
    # uri /airport/MYR
    # airport parameter in URL matches airport_info function
    path('<str:airport_code>', views.airport_info),
]
