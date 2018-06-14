from django.db import models
from django.contrib.auth.models import User


class Patient(models.Model):
    firstname = models.CharField(max_length=30, blank=False)
    lastname = models.CharField(max_length=60, blank=False)
    id_no = models.SlugField(max_length=11, blank=False, unique=True)
    phone = models.CharField(max_length=12, blank=True)
    email = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(default='default_patient_img.png', blank=True)
    history = models.TextField(blank=True)
    doctor = models.ForeignKey(User, default=None, on_delete=models.CASCADE, )

    def __str__(self):
        return "{} {}   ({})".format(self.lastname, self.firstname, self.id_no)
