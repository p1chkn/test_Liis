from rest_framework import serializers

from .models import BookingList


class BookingListSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('workplace', 'datetime_from', 'datetime_to', 'author')
        model = BookingList
