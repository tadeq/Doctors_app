from django import forms
from . import models


class PatientAddForm(forms.ModelForm):
    class Meta:
        model = models.Patient
        fields = ['firstname', 'lastname', 'id_no', 'phone', 'email', 'photo', 'history']
