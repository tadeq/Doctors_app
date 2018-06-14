from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from .models import Patient


# Create your views here.

def patients_list(request):
    patients = Patient.objects.all().order_by('lastname', 'firstname')
    return render(request, "patients/patients_list.html", {'patients': patients})


def add_patient(request):
    if request.method == 'POST':
        form = forms.PatientAddForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.doctor = request.user
            instance.save()
            return redirect('patients:list')
    else:
        form = forms.PatientAddForm()
    return render(request, "patients/patient_add.html", {'form': form})


def patient_details(request, id_no):
    patient = Patient.objects.get(id_no=id_no)
    return render(request, "patients/patient_details.html", {'patient': patient})


def edit_patient(request, id_no):
    patient = get_object_or_404(Patient, id_no=id_no)
    if request.method == 'POST':
        form = forms.PatientAddForm(request.POST, instance=patient)
        if form.is_valid():
            patient = form.save()
            return redirect("patients:details", id_no=patient.id_no)
    else:
        form = forms.PatientAddForm(instance=patient)
    return render(request, "patients/patient_edit.html", {'form': form, 'patient': patient})
