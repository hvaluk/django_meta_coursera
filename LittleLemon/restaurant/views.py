from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets 
from rest_framework import permissions
from .serializers import  BookingSerializer, MenuItemSerializer
from .models import MenuItem, Booking
from django.http import HttpResponse

def test_view(request):
    return HttpResponse("Hello, world!")


# Create your views here. 
def index(request):
    return render(request, 'index.html')

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class MenuItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    
class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

