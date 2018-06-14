from django.shortcuts import render, redirect
from . import forms
from .models import Workday, Appointment
import datetime


# Create your views here.
def days_list(request):
    days = Workday.objects.all().order_by('date')
    new_form = forms.WorkdayAddForm()
    if request.method == 'POST':
        form = forms.WorkdayAddForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            day_good = True
            if instance.date < datetime.datetime.date(datetime.datetime.now()):
                day_good = False
            if instance.start >= instance.end:
                day_good = False
            for day in days:
                if instance.date == day.date:
                    day_good = False
            if day_good:
                instance.doctor = request.user
                instance.save()
                return redirect('schedule:list')
    return render(request, "schedule/days_list.html", {'days': days, 'form': new_form})


def day_details(request, slug):
    day = Workday.objects.get(slug=slug)
    appointments = Appointment.objects.filter(workday=day).order_by('fr')
    new_form = forms.AppointmentAddForm()
    if request.method == 'POST':
        form = forms.AppointmentAddForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            time_good = True
            if instance.fr >= instance.to or instance.fr < day.start or instance.to > day.end:
                time_good = False
            for appointment in appointments:
                if appointment.fr < instance.fr < appointment.to or appointment.fr < instance.to < appointment.to or \
                        instance.fr <= appointment.fr <= instance.to or instance.fr <= appointment.to <= instance.to:
                    time_good = False
            if time_good:
                instance.workday = day
                instance.save()
                return redirect('schedule:details', slug=day.slug)
    return render(request, "schedule/day_details.html", {'day': day, 'appointments': appointments, 'form': new_form})
