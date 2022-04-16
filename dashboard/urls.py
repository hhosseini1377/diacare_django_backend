from django.urls import path

from .views.experts import DoctorVisits
from .views.patients import PatientRetrieveVisitHistory, PatientFullRetrieveVisit

app_name = 'dashboard'

urlpatterns = [
    path('doctorvisits/', DoctorVisits.as_view(), name='free_diet_view'),
    path('patient/visits/history/', PatientRetrieveVisitHistory.as_view(), name='dashboard-history'),
    path('patient/visits/<int:pk>/', PatientFullRetrieveVisit.as_view(), name='dashborad-retrieve-visit')
]