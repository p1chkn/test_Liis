from rest_framework import viewsets

from .models import BookingList
from .serializers import BookingListSerializer


class BookingListViewSet(viewsets.ModelViewSet):

    queryset = BookingList.objects.all()
    serializer_class = BookingListSerializer

    def get_queryset(self):
        queryset = BookingList.objects.filter(author=self.request.user).all()
        return queryset
