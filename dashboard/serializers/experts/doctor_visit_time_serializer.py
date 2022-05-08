import rest_framework.serializers as serializers
from django.utils import timezone
from rest_framework.serializers import ModelSerializer

from diabetes_control.models import VisitTime


class DoctorVisitTimeSerializer(ModelSerializer):
    patient_first_name = serializers.CharField(source='patient.first_name', allow_null=True)
    patient_last_name = serializers.CharField(source='patient.last_name', allow_null=True)
    is_passed = serializers.SerializerMethodField('is_visit_passed')

    # @staticmethod
    def is_visit_passed(self, obj):
        if obj.start_date > timezone.now():
            return False
        return True

    class Meta:
        model = VisitTime
        fields = ['id', 'start_date', 'end_date', 'patient_first_name', 'patient_last_name', 'is_passed']
