''' Handles the Table Booking feature '''
from datetime import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Booking


# pylint: disable=too-few-public-methods
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

    # Prevent Users from booking a table in the past
    def clean(self):
        cleaned_data = super().clean()
        booking_date = cleaned_data.get('booking_date')
        booking_time = cleaned_data.get('booking_timeslot')

        try:
            booking_datetime = datetime.combine(booking_date, booking_time)
            booking_datetime_aware = timezone.make_aware(
                booking_datetime, timezone.get_current_timezone())
        except TypeError as exc:
            raise ValidationError("Invalid date or time format.") from exc

        current_datetime = timezone.now()

        if booking_datetime_aware < current_datetime:
            raise ValidationError(
                "Please select a date and time in the future.")
        return cleaned_data
