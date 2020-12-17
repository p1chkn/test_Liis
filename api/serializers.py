from rest_framework import serializers

from .models import BookingList


class BookingListSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('workplace', 'datetime_from', 'datetime_to', 'author')
        model = BookingList
    
    def validate(self, attrs):
        if attrs['datetime_from'] > attrs['datetime_to']:
            raise serializers.ValidationError('Date_from more than date_to')
        return attrs
