from random import choices
from string import ascii_letters, digits, ascii_uppercase
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from user.models import User


class Booking(models.Model):
    bookingID = models.CharField(max_length=10, primary_key=True, editable=False)

    vehicle = models.CharField(max_length=32)
    vehicle_registration_id = models.CharField(max_length=32, editable=False)

    renter = models.ForeignKey(User, on_delete=models.CASCADE)

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        default=200,
        editable=False,
    )

    discount = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        blank=True,
        default=20,
        editable=False,
    )

    booked_on = models.DateTimeField(auto_now_add=True)

    starting_date = models.DateField()
    duration = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.vehicle} [{self.vehicle_registration_id}]"

    def save(self, *args, **kwargs):
        if not self.bookingID:
            self.bookingID = "".join(choices(ascii_letters + digits, k=6))

        self.price = float(1000 * int(self.duration)) * (1 - self.discount / 100)

        if not self.vehicle_registration_id:
            self.vehicle_registration_id = (
                "".join(choices(ascii_uppercase, k=2))
                + "".join(choices(digits, k=2))
                + " "
                + "".join(choices(ascii_uppercase, k=1))
                + " "
                + "".join(choices(digits, k=4))
            )

        super(Booking, self).save(*args, **kwargs)
