from django.shortcuts import render

from rest_framework import viewsets
from .models import Client, SportsHall, AvailableSlot, Booking
from .serializers import ClientSerializer, SportsHallSerializer, AvailableSlotSerializer, BookingSerializer

def index(request):
    return render(request, 'booking/index.html')

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class SportsHallViewSet(viewsets.ModelViewSet):
    queryset = SportsHall.objects.all()
    serializer_class = SportsHallSerializer

class AvailableSlotViewSet(viewsets.ModelViewSet):
    queryset = AvailableSlot.objects.all()
    serializer_class = AvailableSlotSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
