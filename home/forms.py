''' Handles the Table Booking feature '''
from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Booking



class TableBookingForm(forms.ModelForm):
    """Form to book a table"""
    class Meta:
        """Meta class"""
        model = Booking
        fields = (
            'guests_count',
            'booking_date',
            'booking_timeslot',
            'notes',
            'booking_name')
        widgets = {
            'booking_date': forms.DateInput(attrs={'type': 'date'}),
            'booking_time': forms.TimeInput(attrs={'type': 'time'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        booking_date = cleaned_data.get('booking_date')
        booking_time = cleaned_data.get('booking_timeslot')

        if booking_date < timezone.now().date():
            raise ValidationError(
                "Please select a date and time in the future")

        if booking_date == timezone.now().date() and booking_time < timezone.now().time():
            raise ValidationError(
                "Booking time cannot be in the past."
                )

        return cleaned_data
