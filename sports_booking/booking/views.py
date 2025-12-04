from django.shortcuts import render, get_object_or_404, redirect

from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Client, SportsHall, AvailableSlot, Booking
from .serializers import ClientSerializer, SportsHallSerializer, AvailableSlotSerializer, BookingSerializer

@api_view(['GET'])
def sportshall_list(request):
    halls = SportsHall.objects.all()
    serializer = SportsHallSerializer(halls, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def availableslot_list(request):
    hall_id = request.GET.get('hall')  # Получаем ID зала из параметров запроса

    if hall_id:
        # Фильтруем слоты по выбранному залу
        slots = AvailableSlot.objects.filter(hall_id=hall_id, is_booked=False)
    else:
        # Если параметр hall не передан, возвращаем все свободные слоты
        slots = AvailableSlot.objects.filter(is_booked=False)

    serializer = AvailableSlotSerializer(slots, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def booking_create(request):
    serializer = BookingSerializer(data=request.data)
    if serializer.is_valid():
        # Проверим, что слот не забронирован
        slot_id = request.data.get('slot')
        slot = get_object_or_404(AvailableSlot, id=slot_id)
        if slot.is_booked:
            return Response({'error': 'Слот уже забронирован'}, status=400)

        # Сохраняем бронирование
        booking = serializer.save()
        slot.is_booked = True
        slot.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def booking_cancel(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.status = 'cancelled'
    booking.slot.is_booked = False
    booking.slot.save()
    booking.save()
    return Response({'status': 'cancelled'})

@api_view(['GET'])
def booking_list(request):
    bookings = Booking.objects.all()
    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data)

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
