from rest_framework import viewsets
from django.shortcuts import get_list_or_404
from .models import BookingList
from .serializers import BookingListSerializer
from rest_framework.response import Response


class BookingListViewSet(viewsets.ModelViewSet):

    queryset = BookingList.objects.all()
    serializer_class = BookingListSerializer

    def retrieve(self, request, pk=None):
        queryset = get_list_or_404(BookingList, workplace=pk)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
