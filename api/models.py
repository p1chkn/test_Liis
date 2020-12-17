from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Workplace(models.Model):
    cabinet_number = models.IntegerField()
    description = models.TextField(blank=True)

    def __str__(self):
        return str(self.cabinet_number)


class BookingList(models.Model):
    workplace = models.ForeignKey(Workplace, on_delete=models.CASCADE)
    datetime_from = models.DateTimeField()
    datetime_to = models.DateTimeField()

    def __str__(self):
        return str(self.workplace.cabinet_number)
