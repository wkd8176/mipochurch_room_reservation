from django.db import models

# Create your models here.


class Reservation(models.Model):
    booker = models.CharField(max_length=10)
    start_time = models.DateTimeField(auto_now=False)
    end_time = models.DateTimeField(auto_now=False)
    participants = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    password = models.CharField(max_length=20)

    def __str__(self):
        return f'[{self.booker}] :: {self.start_time} ~ {self.end_time}'
