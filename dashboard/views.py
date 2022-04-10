from django.utils import timezone
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from diabetes_control.models import VisitTime
from diabetes_control.serializers import DoctorVisitTimeSerializer
from _helpers.custom_permisions import IsDoctor


class DoctorVisits(APIView):
    permission_classes = [IsAuthenticated, IsDoctor]

    def get(self, request):
        visits = VisitTime.objects.filter(doctor=request.user).order_by('start_date')
        ahead_visit_times_serializer = DoctorVisitTimeSerializer(visits, many=True)
        return Response(ahead_visit_times_serializer.data)
