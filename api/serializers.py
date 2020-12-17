import datetime

from rest_framework import serializers

from .models import BookingList


class BookingListSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('workplace', 'datetime_from', 'datetime_to', 'author')
        model = BookingList

    def validate(self, attrs):
        date_from = attrs['datetime_from']
        date_to = attrs['datetime_to']
        if date_from > date_to:
            raise serializers.ValidationError('Date_from more than date_to')
        queryset = BookingList.objects.filter(workplace=attrs['workplace'])
        time_list = []
        for item in queryset:
            temp = [item.datetime_from, item.datetime_to]
            time_list.append(temp)
        time_list.sort()
        for i in range(len(time_list)):
            if date_to < time_list[i][0]:
                continue
            elif date_from > time_list[i][1]:
                continue
            elif date_from > time_list[i][0] and date_from < time_list[i][1]:
                raise serializers.ValidationError(
                            'This date is booked already!')
            elif date_to > time_list[i][0] and date_to < time_list[i][1]:
                raise serializers.ValidationError(
                            'This date is booked already!')
            elif date_to > time_list[i][1] and date_from < time_list[i][0]:
                raise serializers.ValidationError(
                            'This date is booked already!')
        return attrs
