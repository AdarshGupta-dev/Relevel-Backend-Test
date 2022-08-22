from .serializers import BookingSerializer
from .models import Booking
from rest_framework import generics

from rest_framework.permissions import IsAuthenticated, IsAdminUser


class BookingCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def perform_create(self, serializer):
        serializer.save(renter=self.request.user)


class BookingDetailAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    lookup_field = "bookingID"

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Booking.objects.filter(renter=self.request.user)
        return Booking.objects.none()


class BookingListAPIView(generics.ListAPIView):
    permission_classes = [IsAdminUser]

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class BookingUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    lookup_field = "bookingID"

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Booking.objects.filter(renter=self.request.user)
        return Booking.objects.none()


class BookingDeleteAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    lookup_field = "bookingID"

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Booking.objects.filter(renter=self.request.user)
        return Booking.objects.none()
