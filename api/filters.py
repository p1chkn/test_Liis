from django_filters import rest_framework as filters

from .models import BookingList


class BookingListFilter(filters.FilterSet):

    datetime_from = filters.DateTimeFilter(field_name='datetime_from',
                                           lookup_expr='gte')
    datetime_to = filters.DateTimeFilter(field_name='datetime_to',
                                         lookup_expr='lte')

    class Meta:
        model = BookingList
        fields = ['datetime_from', 'datetime_to']
