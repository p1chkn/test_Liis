from rest_framework import serializers

from .models import BookingList


class BookingListSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = BookingList
