from django.urls import path
from . import views

app_name = 'patients'

urlpatterns = [
    path('', views.patients_list, name="list"),
    path('add', views.add_patient, name="add"),
    path('<slug:id_no>', views.patient_details, name="details"),
    path('<slug:id_no>/edit/', views.edit_patient, name="edit")
]
