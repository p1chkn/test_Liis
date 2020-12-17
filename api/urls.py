from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .views import BookingListViewSet

booking_router = DefaultRouter()
booking_router.register('v1/booking', BookingListViewSet)

urlpatterns = [
    path('v1/token/', TokenObtainPairView.as_view()),
    path('v1/token/refresh', TokenRefreshView.as_view()),
    path('', include(booking_router.urls)),
]
