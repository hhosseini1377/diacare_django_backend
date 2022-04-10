import logging
from django.utils import timezone
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response

from _helpers.caches import cache_for
from account.models import Account
from diabetes_control.models import VisitTime

logger = logging.getLogger(__name__)


class GetLandingPageInformation(RetrieveAPIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, *args, **kwargs):
        data = self._get_counts()
        return Response(data=data)

    @staticmethod
    @cache_for(10 * 60)
    def _get_counts():
        patients_num = Account.objects.filter(role=Account.PATIENT).count()
        experts_num = Account.objects.filter(role=Account.EXPERT).count()
        done_visits_num = VisitTime.objects.filter(start_date__lte=timezone.now()).count()
        return {'patients_count': patients_num, 'experts_count': experts_num, 'done_visits_count': done_visits_num}

    def get_queryset(self):
        return Account.objects.all()
