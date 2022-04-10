from .views import DoctorVisits
from django.urls import path

app_name = 'free_diet'

urlpatterns = [
    path('doctorvisits/', DoctorVisits.as_view(), name='free_diet_view')
]