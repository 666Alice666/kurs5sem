from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, SportsHallViewSet, AvailableSlotViewSet, BookingViewSet
from . import views

router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'sportshalls', SportsHallViewSet)
router.register(r'availableslots', AvailableSlotViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('', include(router.urls)),
]