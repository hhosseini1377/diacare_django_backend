from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from diabetes_control.models import DietTemplatePart
from rest_framework import status
from diabetes_control.models import VisitTime
from datetime import timedelta, datetime
from diabetes_control.serializers import DoctorVisitTimeSerializer


class DoctorAheadVisits(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        print(request.user)
        visits = VisitTime.objects.filter(doctor=request.user, start_date__gt=datetime.now()).order_by('start_date')
        ahead_visit_times_serializer = DoctorVisitTimeSerializer(visits, many=True)
        return Response(ahead_visit_times_serializer.data)
