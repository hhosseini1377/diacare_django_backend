from django.urls import path

from diabetes_control.views.doctors import ListAvailableVisitsReturnPerDoctorsView, ListAvailableVisitsPerDateTimeView

app_name = 'diabetes_control'

urlpatterns = [
    path('visits/available/retrieve/per_doctor', ListAvailableVisitsReturnPerDoctorsView.as_view(),
         name="retrieve-visits-group-by-doctors"),
    path('visits/available/retrieve/<int:doctor_id>', ListAvailableVisitsPerDateTimeView.as_view(),
         name="retrieve-visits-per-time-fixed-doctor")
]
