from django.utils import timezone
from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination

from _helpers.custom_permisions import IsPatient
from dashboard.serializers.patients import PatientFutureVisitTimeSerializer
from diabetes_control.models import VisitTime


class PatientRetrieveFutureVisit(ListAPIView):
    permission_classes = [IsPatient, ]
    pagination_class = LimitOffsetPagination
    serializer_class = PatientFutureVisitTimeSerializer

    def get_queryset(self):
        _q = VisitTime.objects.filter(patient=self.request.user, start_date__gte=timezone.now()).order_by('-start_date')
        return _q
