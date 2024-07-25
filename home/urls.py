from . import views
from django.urls import path

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('menus/food_menu/', views.FoodMenu.as_view(), name='food_menu'),
    path('menus/drinks_menu/', views.DrinksMenu.as_view(), name='drinks_menu'),
    path('booking/new/', views.BookingView.as_view(), name='booking'),
    path(
        'bookings_list/',
        views.UserBookingsList.as_view(),
        name='bookings_list'
    ),
    path(
        'edit_booking/<int:pk>',
        views.EditBookingView.as_view(),
        name='edit_booking'
    ),
    path(
        'delete_booking/<int:id>',
        views.DeleteBookingView.as_view(),
        name='delete_booking'
        ),
    path(
        'booking/confirmation/',
        views.ConfirmationView.as_view(),
        name='confirmation_page'
        ),
]
