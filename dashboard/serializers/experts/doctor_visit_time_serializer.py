import rest_framework.serializers as serializers
from rest_framework.serializers import ModelSerializer

from diabetes_control.models import VisitTime


class DoctorVisitTimeSerializer(ModelSerializer):
    patient_first_name = serializers.CharField(source='patient.first_name')
    patient_last_name = serializers.CharField(source='patient.last_name')

    class Meta:
        model = VisitTime
        fields = ['id', 'start_date', 'patient_first_name', 'patient_last_name']
