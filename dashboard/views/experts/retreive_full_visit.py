from rest_framework.generics import RetrieveAPIView

from _helpers.custom_permisions import IsDoctor
from dashboard.serializers.patients import DoctorVisitTimeSerializer
from diabetes_control.models import VisitTime


class DoctorFullRetrieveVisit(RetrieveAPIView):
    permission_classes = [IsDoctor, ]
    serializer_class = DoctorVisitTimeSerializer

    def get_queryset(self):
        return VisitTime.objects.filter(doctor=self.request.user)
