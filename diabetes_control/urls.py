from django.urls import path

from diabetes_control.views import AddPatientToVisitView
from diabetes_control.views.doctors import ListAvailableVisitsReturnPerDoctorsView, ListAvailableVisitsPerDateTimeView

app_name = 'diabetes_control'

urlpatterns = [
    path('visits/available/search/per_doctor', ListAvailableVisitsReturnPerDoctorsView.as_view(),
         name="retrieve-visits-group-by-doctors"),
    path('visits/available/retrieve/', ListAvailableVisitsPerDateTimeView.as_view(),
         name="retrieve-visits-per-time-fixed-doctor"),
    path('visits/add_patient/<int:pk>', AddPatientToVisitView.as_view(), name='add-patient-to-visit')
]
