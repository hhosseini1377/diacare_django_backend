from .views import DoctorAheadVisits
from django.urls import path

app_name = 'free_diet'

urlpatterns = [
    path('doctoraheadvisits/', DoctorAheadVisits.as_view(), name='free_diet_view')
]