from django.http import JsonResponse
from django.shortcuts import get_list_or_404
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .filters import BookingListFilter
from .models import BookingList, Workplace
from .permissions import IsOwnerOrReadOnly
from .serializers import BookingListSerializer, WorkplaceSerializer


@api_view(['GET'])
def workplace(request):

    data = Workplace.objects.all()
    serializer = WorkplaceSerializer(data, many=True)
    return JsonResponse(serializer.data)


class BookingListViewSet(viewsets.ModelViewSet):

    queryset = BookingList.objects.select_related('workplace', 'author').all()
    serializer_class = BookingListSerializer
    permission_classes = [IsOwnerOrReadOnly]
    filter_class = BookingListFilter

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def retrieve(self, request, pk=None):
        queryset = get_list_or_404(BookingList, workplace=pk)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
