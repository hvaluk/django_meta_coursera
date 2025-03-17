from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1> Welcome to Little Lemon! </h1>')

def about(request):
    return HttpResponse("<h1> About us </h1>")

def menu(request):
    return HttpResponse("<h1> Menu </h1>")

def book(request):
    return HttpResponse("<h1> Make a booking </h1>")