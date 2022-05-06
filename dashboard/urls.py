from django.urls import path

from .views.experts import DoctorVisits, DoctorFullRetrieveVisit
from .views.patients import PatientRetrieveVisitHistory, PatientFullRetrieveVisit, PatientRetrieveFutureVisit, \
    RetrieveListFreeDiets, GetFreeDietView

app_name = 'dashboard'

urlpatterns = [
    path('doctorvisits/', DoctorVisits.as_view(), name='free_diet_view'),
    path('patient/visits/history/', PatientRetrieveVisitHistory.as_view(), name='dashboard-history-patient'),
    path('patient/visits/future/', PatientRetrieveFutureVisit.as_view(), name='dashboard-future-patient'),
    path('patient/visits/<int:pk>/', PatientFullRetrieveVisit.as_view(), name='dashborad-retrieve-visit'),
    path('doctor/visits/<int:pk>/', DoctorFullRetrieveVisit.as_view(), name='dashborad-retrieve-visit-doctor'),
    path('patient/free_diets/', RetrieveListFreeDiets.as_view(), name='dashboard-retrieve-free-diets-patient'),
    path('patient/free_diets/<int:pk>', GetFreeDietView.as_view(), name='dashborad-get-free-diet-patient'),

]
