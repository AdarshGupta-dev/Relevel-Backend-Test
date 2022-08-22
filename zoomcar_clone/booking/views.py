from .serializers import BookingSerializer
from .models import Booking
from rest_framework import generics

from rest_framework.permissions import IsAuthenticated, IsAdminUser


class BookingCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class BookingDetailAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    lookup_field = "bookingID"


class BookingListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class BookingUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    lookup_field = "bookingID"


class BookingDeleteAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    lookup_field = "bookingID"
