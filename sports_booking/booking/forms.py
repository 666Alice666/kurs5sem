from django import forms
from .models import AvailableSlot, Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['slot']

    def __init__(self, hall_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['slot'].queryset = AvailableSlot.objects.filter(
            hall_id=hall_id, is_booked=False
        )