from django.urls import path

from . import views

urlpatterns = [
    path(
        "create/",
        views.BookingCreateAPIView.as_view(),
        name="Book a vehicle",
    ),
    path(
        "detail/<str:bookingID>/",
        views.BookingDetailAPIView.as_view(),
        name="Booking detail",
    ),
    path(
        "list/",
        views.BookingListAPIView.as_view(),
        name="All Bookings",
    ),
    path(
        "update/<str:bookingID>/",
        views.BookingUpdateAPIView.as_view(),
        name="Change Booking",
    ),
    path(
        "delete/<str:bookingID>/",
        views.BookingDeleteAPIView.as_view(),
        name="Cancel Booking",
    ),
]
