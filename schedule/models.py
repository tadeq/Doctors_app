from django.db import models
from django.contrib.auth.models import User
from patients.models import Patient
import datetime
from django.template.defaultfilters import slugify


# Create your models here.
class Workday(models.Model):
    slug = models.SlugField(unique=True)
    date = models.DateField(default=str(datetime.datetime.date(datetime.datetime.now())))
    start = models.TimeField(blank=False)
    end = models.TimeField(blank=False)
    doctor = models.ForeignKey(User, default=None, on_delete=models.CASCADE, )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.date) + slugify(self.doctor)
        super(Workday, self).save(*args, **kwargs)

    def __str__(self):
        return "{} {} {}".format(self.doctor.first_name, self.doctor.last_name, self.date)


class Appointment(models.Model):
    workday = models.ForeignKey(Workday, default=None, on_delete=models.CASCADE, )
    fr = models.TimeField(blank=False)
    to = models.TimeField(blank=False)
    patient = models.ForeignKey(Patient, default=None, on_delete=models.CASCADE, )

    def __str__(self):
        return "{} {} {} {} {} {}".format(self.workday.date, self.fr, self.to, self.patient.lastname,
                                          self.patient.firstname, self.patient.id_no)
