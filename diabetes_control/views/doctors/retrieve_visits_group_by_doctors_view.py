from typing import Optional

from django.contrib.auth import get_user_model
from django.db.models import Count
from django.db.models import F
from django.db.models import Q
from django_plus.api import UrlParam as _p
from rest_framework.generics import GenericAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from _helpers.caches import cache_for
from _helpers.custom_permisions import IsPatient
from diabetes_control.models import VisitTime

User = get_user_model()


class ListAvailableVisitsReturnPerDoctorsView(GenericAPIView):
    permission_classes = (IsPatient,)
    pagination_class = LimitOffsetPagination
    list_params_template = [
        _p('name', _p.string),
        _p('date', _p.date)
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance = None  # type: Optional[VisitTime]

    def get(self, request, *args, **kwargs):
        _q = self.get_queryset()
        data = self._get_objects(_q)
        data['results'] = self.paginate_queryset(data['results'])
        data['limit'] = self.request.query_params.get('limit', 0)
        data['offset'] = self.request.query_params.get('offset', 0)
        return Response(data)

    @staticmethod
    @cache_for(10 * 60)
    def _get_objects(_q):
        data = {}
        data['results'] = _q.values('doctor').annotate(available_times=Count('doctor'), doctor_email=F('doctor__email'),
                                            doctor_name=F('doctor__first_name'),
                                            doctor_last_name=F('doctor__last_name')).order_by('-available_times')

        data['count'] = data['results'].count()
        return data

    def get_queryset(self):
        _q = Q()
        date = _p.clean_data(self.request.query_params, self.list_params_template)['date']
        name = _p.clean_data(self.request.query_params, self.list_params_template)['name']
        if date:
            _q |= Q(start_date__startswith=date)
        if name:
            _q |= Q(doctor__last_name__icontains=name)
        return VisitTime.objects.filter(_q)
