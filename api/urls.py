from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import BookingListViewSet

booking_router = DefaultRouter()
booking_router.register('v1/booking', BookingListViewSet)

urlpatterns = [
    path('', include(booking_router.urls)),
]