from django.http import HttpResponse, Http404
from django.shortcuts import render

# from this current models module - package
from .models import Flight

# Create your views here.
def index(request):
    # return HttpResponse("Welcome to DjangoAir!")
    # render takes a couple of arguments, the request and the html template, context
    context = {
        "flights": Flight.objects.all()
    }
    return render(request, "flights/index.html", context)

def flight(request, flight_id):
    try:
        flight = Flight.objects.get(pk=flight_id)
    except Flight.DoesNotExist:
        raise Http404("Flight does not exist.")
    context = {
        "flight": flight
    }
    return render(request, "flights/flight.html", context)