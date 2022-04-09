from typing import Optional

from rest_framework.generics import ListAPIView

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
        return VisitTime.objects.filter(doctor=self.kwargs['doctor_id'], doctor__role=Account.EXPERT)
