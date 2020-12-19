from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import api_view

from .filters import BookingListFilter
from .models import BookingList, Workplace
from .permissions import IsOwnerOrReadOnly
from .serializers import BookingListSerializer, WorkplaceSerializer


@api_view(['GET'])
def workplace(request):

    data = Workplace.objects.all()
    serializer = WorkplaceSerializer(data, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def workplace_bookinglist(request, workplace_id):

    workplace = get_object_or_404(Workplace, id=workplace_id)
    data = BookingList.objects.filter(workplace=workplace).all()
    serializer = BookingListSerializer(data, many=True)
    return JsonResponse(serializer.data, safe=False)


class BookingListViewSet(viewsets.ModelViewSet):

    queryset = BookingList.objects.select_related('workplace', 'author').all()
    serializer_class = BookingListSerializer
    permission_classes = [IsOwnerOrReadOnly]
    filter_class = BookingListFilter

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
