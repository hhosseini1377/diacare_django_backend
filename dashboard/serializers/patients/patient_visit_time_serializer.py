import rest_framework.serializers as serializers
from rest_framework.serializers import ModelSerializer

from diabetes_control.models import VisitTime, Prescription, DietTemplatePart, SpecializedDiet


class PrescriptionSerializer(ModelSerializer):
    context = serializers.CharField()

    class Meta:
        model = Prescription
        fields = ['context']


class DietPartsSerializer(ModelSerializer):
    class Meta:
        model = DietTemplatePart
        fields = ['week_day', 'meal', 'context']


class SpecializedDietSerializer(ModelSerializer):
    diet_parts = DietPartsSerializer(many=True, source='diettemplatepart_set')

    class Meta:
        model = SpecializedDiet
        fields = ['name', 'diet_parts']


class PatientHistoryVisitTimeSerializer(ModelSerializer):
    doctor_first_name = serializers.CharField(source='doctor.first_name')
    doctor_last_name = serializers.CharField(source='doctor.last_name')
    prescription = PrescriptionSerializer(read_only=True)
    specialized_diet = serializers.CharField(source='specializeddiet.name')

    class Meta:
        model = VisitTime
        fields = ['id', 'start_date', 'end_date', 'doctor_first_name', 'doctor_last_name', 'prescription',
                  'specialized_diet']


class PatientVisitTimeSerializer(ModelSerializer):
    doctor_first_name = serializers.CharField(source='doctor.first_name')
    doctor_last_name = serializers.CharField(source='doctor.last_name')
    prescription = PrescriptionSerializer(read_only=True)
    specialized_diet = SpecializedDietSerializer(source='specializeddiet')

    class Meta:
        model = VisitTime
        fields = ['id', 'start_date', 'end_date', 'doctor_first_name', 'doctor_last_name', 'prescription',
                  'specialized_diet']


class DoctorVisitTimeSerializer(ModelSerializer):
    doctor_first_name = serializers.CharField(source='patient.first_name')
    doctor_last_name = serializers.CharField(source='patient.last_name')
    prescription = PrescriptionSerializer(read_only=True)
    specialized_diet = SpecializedDietSerializer(source='specializeddiet')

    class Meta:
        model = VisitTime
        fields = ['id', 'start_date', 'end_date', 'doctor_first_name', 'doctor_last_name', 'prescription',
                  'specialized_diet']

class PatientFutureVisitTimeSerializer(ModelSerializer):
    doctor_first_name = serializers.CharField(source='doctor.first_name')
    doctor_last_name = serializers.CharField(source='doctor.last_name')

    class Meta:
        model = VisitTime
        fields = ['id', 'start_date', 'end_date', 'doctor_first_name', 'doctor_last_name']
