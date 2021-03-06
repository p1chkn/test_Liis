from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Workplace(models.Model):

    cabinet_number = models.IntegerField()
    description = models.TextField(blank=True)

    def __str__(self):
        return str(self.id)


class BookingList(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    workplace = models.ForeignKey(Workplace, on_delete=models.CASCADE)
    datetime_from = models.DateTimeField()
    datetime_to = models.DateTimeField()

    def __str__(self):
        return str(self.workplace.id)
