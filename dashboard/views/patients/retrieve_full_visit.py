from rest_framework.generics import RetrieveAPIView

from _helpers.custom_permisions import IsPatient
from dashboard.serializers.patients import PatientVisitTimeSerializer
from diabetes_control.models import VisitTime


class PatientFullRetrieveVisit(RetrieveAPIView):
    permission_classes = [IsPatient, ]
    serializer_class = PatientVisitTimeSerializer

    def get_queryset(self):
        return VisitTime.objects.filter(patient=self.request.user)
