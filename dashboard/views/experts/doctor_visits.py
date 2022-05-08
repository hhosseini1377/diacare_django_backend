from datetime import datetime

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from _helpers.custom_permisions import IsDoctor
from dashboard.serializers.experts import DoctorVisitTimeSerializer
from diabetes_control.models import VisitTime

from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination


class DoctorVisitsHistory(ListAPIView):
    permission_classes = [IsDoctor, ]
    serializer_class = DoctorVisitTimeSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        _q = VisitTime.objects.filter(doctor=self.request.user).order_by('-start_date')
        return _q


class DoctorAheadVisits(ListAPIView):
    permission_classes = [IsDoctor, ]
    serializer_class = DoctorVisitTimeSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        _q = VisitTime.objects.filter(doctor=self.request.user, start_date__gt=datetime.now()).order_by('start_date')
        return _q
