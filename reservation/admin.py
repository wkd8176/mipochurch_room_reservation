from django.contrib import admin
from .models import Reservation, Notice

# Register your models here.
admin.site.register(Reservation)
admin.site.register(Notice)
