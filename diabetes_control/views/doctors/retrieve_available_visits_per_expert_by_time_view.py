from typing import Optional

from django.utils.dateparse import parse_date
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from _helpers.custom_permisions import IsPatient
from account.models import Account
from diabetes_control.models import VisitTime
from diabetes_control.serializers import GetAvailableVisits


class ListAvailableVisitsPerDateTimeView(ListAPIView):
    permission_classes = (IsPatient,)
    serializer_class = GetAvailableVisits

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance = None  # type: Optional[VisitTime]

    def get_queryset(self):
        doctor_id = self.request.POST.get('doctor_id', None)
        date = parse_date(self.request.POST.get('date', None))
        return VisitTime.objects.filter(doctor=doctor_id,
                                        start_date__date=date, patient__isnull=True)

    def post(self, request, *args, **kwargs):
        doctor_id = self.request.POST.get('doctor_id', None)
        date = self.request.POST.get('date', None)
        if doctor_id is None or date is None:
            return Response(status=status.HTTP_403_FORBIDDEN, data='you should send both date and doctor_id ')
        return self.list(request, *args, **kwargs)
