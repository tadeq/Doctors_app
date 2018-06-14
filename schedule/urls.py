from django.urls import path
from . import views

app_name = 'schedule'

urlpatterns = [
    path('', views.days_list, name="list"),
    path('<slug:slug>', views.day_details, name="details")
]