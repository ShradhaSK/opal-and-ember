'''Handles the Views for all the pages  '''

from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.core.paginator import Paginator
from django.views import generic, View
from .models import Booking, FoodMenuItem, DrinksMenuItem
from django.views.generic.edit import CreateView, UpdateView
from django.utils import timezone

# Import form for the Booking model
from .forms import TableBookingForm

# Create your views here.


class Home(View):
    """
    Displays the Home page in the browser
    """
    def get(self, request):
        return render(request, 'index.html')


class FoodMenu(generic.ListView):
    """
    Displays the Food Menu
    """
    model = FoodMenuItem
    template_name = "menus/food_menu.html"

    def get(self, request):
        appetizers = self.model.objects.filter(category=1)
        main_courses = self.model.objects.filter(category=2)
        desserts = self.model.objects.filter(category=3)

        context = {
            'appetizers': appetizers,
            'main_courses': main_courses,
            'desserts': desserts,
        }
        return render(request, self.template_name, context)


class DrinksMenu(generic.ListView):
    """
    Displays the Food Menu
    """
    model = DrinksMenuItem
    template_name = "menus/drinks_menu.html"
    context_object_name = 'drinks_list'

    def get(self, request):
        tap_beers = self.model.objects.filter(category=4)
        bottle_beers = self.model.objects.filter(category=5)
        whiskeys = self.model.objects.filter(category=6)
        cocktails = self.model.objects.filter(category=7)
        wines = self.model.objects.filter(category=8)
        apertifs = self.model.objects.filter(category=9)
        alcohol_free = self.model.objects.filter(category=10)

        context = {
            'tap_beers': tap_beers,
            'bottle_beers': bottle_beers,
            'whiskeys': whiskeys,
            'cocktails': cocktails,
            'apertifs': apertifs,
            'wines': wines,
            'alcohol_free': alcohol_free,
        }
        return render(request, self.template_name, context)


class BookingView(CreateView):
    """
    Displays the Table Booking form
    """
    form_class = TableBookingForm
    template_name = 'booking.html'

    def get(self, request, *args, **kwargs):
        """
        Renders the Booking form
        """
        booking_form = TableBookingForm()
        return render(request, 'booking.html',
                      {'booking_form': booking_form})

    def post(self, request):
        """
        Checks that the provided info is valid format
        and then posts to database
        """
        booking_form = TableBookingForm(data=request.POST)

        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.booking_user = request.user
            booking.save()
            messages.success(
                request, "Booking succesful!")
            return render(request, 'confirmation_page.html')

        return render(request, 'booking.html',
                      {'booking_form': booking_form})


class UserBookingsList(generic.ListView):
    """
        Navigates to the user's My Bookings page, where the get method
        retrieves all reservations made by logged-in user
        in ascending order by created date.
    """

    template_name = 'bookings_list.html'
    context_object_name = 'reservations'
    paginate_by = 10

    def get_queryset(self):
        now = timezone.now()
        return Booking.objects.filter(
            booking_user=self.request.user,
            booking_date__gte=now.date()
        ).exclude(
            booking_date=now.date(), booking_timeslot__lt=now.time()
        ).order_by('booking_date', 'booking_timeslot')


class EditBookingView(UpdateView):
    """
    This view will display the booking by it's id
    so the user can then edit it
    """

    model = Booking
    form_class = TableBookingForm
    id = id
    template_name = 'edit_booking.html'
    success_message = 'Your Booking has been updated.'

    def form_valid(self, form):
        # Displays the success message upon successful edit
        messages.success(self.request, self.success_message)
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse('bookings_list')


# Deletes the booking the user wishes to cancel

class DeleteBookingView(View):
    """
    Deletes the selected booking by its id
    """

    def get(self, request, id):
        reservation = get_object_or_404(
            Booking,
            id=id,
            booking_user=request.user
        )
        return render(
            request,
            'delete_booking.html',
            {'reservation': reservation}
        )

    def post(self, request, id):
        reservation = get_object_or_404(
            Booking,
            id=id,
            booking_user=request.user
        )
        reservation.delete()
        messages.success(
                request, "Booking Canceled")
        return redirect('bookings_list')  # Red. to the reservations list


class ConfirmationView(View):
    """
    View for handling the confirmation page
    after a successful booking.
    """
    template_name = 'confirmation_page.html'

    def get(self, request):
        return render(request, 'confirmation_page.html')
