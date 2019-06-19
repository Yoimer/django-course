from django.http import HttpResponse
from django.shortcuts import render

# Create your views here

# this returns a simple http response which is a  literal string
def index(request):
    return HttpResponse("Hello, world!")