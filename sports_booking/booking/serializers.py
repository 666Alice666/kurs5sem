from rest_framework import serializers
from .models import Client, SportsHall, AvailableSlot, Booking

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'username', 'email', 'full_name', 'phone_number']

class SportsHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = SportsHall
        fields = ['id', 'name', 'description', 'address', 'capacity', 'price_per_hour', 'is_active']

class AvailableSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailableSlot
        fields = ['id', 'hall', 'available_date', 'start_time', 'end_time', 'is_booked']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'client', 'slot', 'status', 'total_price']