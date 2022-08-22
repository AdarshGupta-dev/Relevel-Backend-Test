from django.contrib import admin

from .models import Booking


class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "bookingID",
        "vehicle",
        "vehicle_registration_id",
        "renter",
        "price",
        "discount",
        "starting_date",
        "duration",
    )

    list_filter = (
        "bookingID",
        "vehicle_registration_id",
        "renter",
        "starting_date",
    )

    search_fields = (
        "bookingID",
        "vehicle_registration_id",
        "renter",
        "starting_date",
    )

    ordering = ("starting_date",)


admin.site.register(Booking, BookingAdmin)
