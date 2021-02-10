from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<H2> Hey! Welcome to Top Deals of the day.</H2>")

# Create your views here.
