from datetime import datetime, time

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import time

# Create your models here.


class Booking(models.Model):
    """
    class for bookings
    """

    TIME_SLOTS = (
        (time(11, 0), '11:00 AM'),
        (time(12, 0), '12:00 PM'),
        (time(13, 0), '01:00 PM'),
        (time(14, 0), '02:00 PM'),
        (time(15, 0), '03:00 PM'),
        (time(19, 0), '07:00 PM'),
        (time(20, 0), '08:00 PM'),
        (time(21, 0), '09:00 PM'),
        (time(22, 0), '10:00 PM'),

    )

    GUESTS_COUNT_CHOICES = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
    )

    booking_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="booking_user"
    )
    guests_count = models.CharField(
        choices=GUESTS_COUNT_CHOICES,
        max_length=2,
        default='2'
    )
    created_on = models.DateTimeField(default=timezone.now, editable=False)
    updated_on = models.DateTimeField(auto_now=True)
    booking_date = models.DateField(default=timezone.now)
    booking_timeslot = models.TimeField(choices=TIME_SLOTS, default=0)
    notes = models.TextField(blank=True, null=True)
    booking_name = models.CharField(max_length=100)

    class Meta:
        """Meta class for Booking model"""
        ordering = ['created_on']

    def __str__(self):
        return f"Booking made by {self.booking_name}"


class FoodMenuItem(models.Model):
    """
    Class for the Food Menu Item Model,
    contains Appetizers, Main Course and Desserts
    """

    class Category(models.IntegerChoices):
        APPETIZERS = 1, 'Appetizers'
        MAINS = 2, 'Main Course'
        DESSERTS = 3, 'Desserts'

    category = models.IntegerField(choices=Category.choices)
    name = models.CharField(
        max_length=100,
        unique=True
    )
    description = models.CharField(
        max_length=200,
        unique=True
    )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta class for Booking model"""
        ordering = ['category']

    def __str__(self):
        return self.name


class DrinksMenuItem(models.Model):
    """
    Class for the Drinks Menu Item Model,
    contains Beers, Cocktails, Whiskey, Apertifs, Wines and alcohol-free drinks
    """

    class Category(models.IntegerChoices):
        BEERS_ON_TAP = 4, 'Beers on Tap'
        BOTTLED_BEERS = 5, 'Bottled Beers'
        WHISKEY = 6, 'Whiskey'
        COCKTAILS = 7, 'Our Signature Cocktails'
        WINES = 8, 'Wines'
        APERTIFS = 9, 'Apertifs'
        ALCOHOL_FREE = 10, 'Alcohol-free Drinks'

    category = models.IntegerField(choices=Category.choices)
    name = models.CharField(
        max_length=100,
        unique=True
    )
    description = models.CharField(
        max_length=200,
        unique=True
    )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta class for Booking model"""
        ordering = ['category']

    def __str__(self):
        return self.name
