from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeTemplateView.as_view(), name="home"),
    path("appointment", views.AppointmentTemplateView.as_view(),
         name="appointment"),
    path("manage-appointments", views.ManageAppointmentListView.as_view(),
         name="manage-appointments")

]
