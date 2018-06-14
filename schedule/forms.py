from django import forms
from . import models


class WorkdayAddForm(forms.ModelForm):
    class Meta:
        model = models.Workday
        fields = ['date', 'start', 'end']


class AppointmentAddForm(forms.ModelForm):
    class Meta:
        model = models.Appointment
        fields = ['fr', 'to', 'patient']
        labels = {
            'fr': 'From',
        }
