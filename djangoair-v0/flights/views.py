from django.http import HttpResponse
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