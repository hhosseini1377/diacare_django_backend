from django.utils import timezone
from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination

from _helpers.custom_permisions import IsPatient
from diabetes_control.models import VisitTime
from dashboard.serializers.patients import PatientHistoryVisitTimeSerializer


class PatientRetrieveVisitHistory(ListAPIView):
    permission_classes = [IsPatient, ]
    pagination_class = LimitOffsetPagination
    serializer_class = PatientHistoryVisitTimeSerializer
    def get_queryset(self):
        _q = VisitTime.objects.filter(patient=self.request.user, start_date__lte=timezone.now()).order_by('-start_date')
        return _q
