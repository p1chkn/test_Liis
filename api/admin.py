from django.contrib import admin

from .models import BookingList, Workplace


class WorkplaceAdmin(admin.ModelAdmin):

    list_display = ('pk', 'cabinet_number', 'description')
    list_filter = ('cabinet_number', )


class BookingListAdmin(admin.ModelAdmin):

    list_display = ('workplace', 'datetime_from', 'datetime_to')
    list_filter = ('workplace', 'datetime_from', 'datetime_to')


admin.site.register(Workplace, WorkplaceAdmin)
admin.site.register(BookingList, BookingListAdmin)
