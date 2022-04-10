from rest_framework import serializers

from diabetes_control.models import VisitTime


class GetAvailableVisits(serializers.ModelSerializer):
    start_date = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M:%S")
    end_date = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M:%S")
    doctor = serializers.CharField()

    class Meta:
        model = VisitTime
        fields = ['id', 'start_date', 'end_date', 'doctor']
