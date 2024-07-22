from django.contrib import admin
from .models import Booking, FoodMenuItem, DrinksMenuItem
from django_summernote.admin import SummernoteModelAdmin
from rangefilter.filters import DateRangeFilter

# Register your models here.

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """
    class to filter and display Booking info
    """
    list_filter = ('created_on', ('booking_date', DateRangeFilter), 'booking_user', 'booking_name',)
    list_display = (
        'id',
        'booking_date',
        'booking_timeslot',
        'booking_name',
        'guests_count',
        'notes',
        'booking_user',
    )
    search_fields = ['booking_name']


@admin.register(FoodMenuItem)
class FoodMenuItemAdmin(admin.ModelAdmin):
    """
    class to filter and display Food Menu items
    """
    list_filter = (('added_on', DateRangeFilter), ('updated_on', DateRangeFilter), 'category',)
    list_display = (
        'id',
        'name',
        'category',
        'added_on',
        'updated_on',
    )
    search_fields = ['name', 'category']
    summernote_fields = ('description')


@admin.register(DrinksMenuItem)
class DrinksMenuItemAdmin(admin.ModelAdmin):
    """
    class to filter and display Drinks Menu items
    """
    list_filter = (('added_on', DateRangeFilter), ('updated_on', DateRangeFilter), 'category',)
    list_display = (
        'id',
        'name',
        'category',
        'added_on',
        'updated_on',
    )
    search_fields = ['name', 'category']
    summernote_fields = ('description')