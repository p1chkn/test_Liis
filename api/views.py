from django.shortcuts import get_list_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from .filters import BookingListFilter
from .models import BookingList
from .permissions import IsOwnerOrReadOnly
from .serializers import BookingListSerializer


class BookingListViewSet(viewsets.ModelViewSet):

    queryset = BookingList.objects.all()
    serializer_class = BookingListSerializer
    permission_classes = [IsOwnerOrReadOnly]
    filter_class = BookingListFilter

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def retrieve(self, request, pk=None):
        queryset = get_list_or_404(BookingList, workplace=pk)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
