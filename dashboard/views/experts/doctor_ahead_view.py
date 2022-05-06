from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from _helpers.custom_permisions import IsDoctor
from dashboard.serializers.experts import DoctorVisitTimeSerializer
from diabetes_control.models import VisitTime


class DoctorVisits(APIView):
    permission_classes = [IsDoctor, ]

    def get(self, request):
        visits = VisitTime.objects.filter(doctor=request.user).order_by('start_date')
        ahead_visit_times_serializer = DoctorVisitTimeSerializer(visits, many=True)
        return Response(ahead_visit_times_serializer.data, status=status.HTTP_200_OK)
