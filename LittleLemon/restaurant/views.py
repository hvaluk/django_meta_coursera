import json
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, viewsets, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Booking, MenuItem
from .forms import BookingForm
from .serializers import BookingSerializer, MenuItemSerializer

def test_view(request):
    return HttpResponse("Hello, world!")

@api_view()
@permission_classes([IsAuthenticated])
def msg(request):
    return Response({"message": "This view is protected"})

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def reservations(request):
    date = request.GET.get('date', datetime.today().date())
    bookings = Booking.objects.all()
    booking_json = serializers.serialize('json', bookings)
    return render(request, 'bookings.html', {"bookings": booking_json})

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'book.html', context)

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class MenuItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

@csrf_exempt
def bookings(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        exist = Booking.objects.filter(
            booking_time__date=data['reservation_date'],
            booking_time__hour=data['reservation_slot']
        ).exists()

        if not exist:
            booking = Booking(
                name=data['first_name'],
                booking_time=f"{data['reservation_date']} {data['reservation_slot']}:00"
            )
            booking.save()
        else:
            return JsonResponse({'error': 1}, status=400)

    date = request.GET.get('date', datetime.today().date())
    bookings = Booking.objects.filter(booking_time__date=date)
    return JsonResponse(list(bookings.values()), safe=False)

