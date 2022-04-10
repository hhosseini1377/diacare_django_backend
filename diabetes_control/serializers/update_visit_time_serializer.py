from rest_framework import serializers

from account.models import Account
from diabetes_control.models import VisitTime


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['pk', 'email', 'first_name', 'last_name']


class VisitTimeUpdateSerializer(serializers.ModelSerializer):
    start_date = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M:%S")
    end_date = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M:%S")
    doctor = AccountSerializer(read_only=True)

    class Meta:
        model = VisitTime
        fields = ['start_date', 'end_date', 'doctor', 'patient']

    def update(self, instance, validated_data):
        if instance.patient is not None:
            raise serializers.ValidationError(
                {"error": "this object is already assigned to another patient, you cannot reallocate it"})
        if self.context['request'].user.role != Account.PATIENT:
            raise serializers.ValidationError({"authorize": "user should be of patient type"})
        return super(VisitTimeUpdateSerializer, self).update(instance, validated_data)

    def to_representation(self, instance):
        ret = super(VisitTimeUpdateSerializer, self).to_representation(instance)
        ret['patient'] = {
            "pk": instance.patient.pk,
            "email": instance.patient.email,
            "first_name": instance.patient.first_name,
            "last_name": instance.patient.last_name
        }
        return ret
