from django.contrib import admin
from .models import Appointment, Workday

# Register your models here.
admin.site.register(Workday)
admin.site.register(Appointment)
