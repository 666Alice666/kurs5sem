from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, SportsHallViewSet, AvailableSlotViewSet, BookingViewSet
from . import views

router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'sportshalls', SportsHallViewSet)
#router.register(r'availableslots', AvailableSlotViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('api/sportshalls/', views.sportshall_list, name='sportshall-list'),
    path('api/availableslots/', views.availableslot_list, name='availableslot-list'),
    path('api/bookings/', views.booking_create, name='booking-create'),  # POST для создания
    path('api/bookings/my-bookings/', views.booking_list, name='booking-list'),  # GET для списка
    path('api/bookings/<int:booking_id>/cancel/', views.booking_cancel, name='booking-cancel'),
    path('', views.index, name='index'),
    path('', include(router.urls)),
    path('api/bookings/', views.booking_list, name='booking-list'),  # POST для создания
]

