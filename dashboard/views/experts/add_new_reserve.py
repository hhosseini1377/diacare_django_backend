from datetime import datetime

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from _helpers.custom_permisions import IsDoctor
from diabetes_control.models import VisitTime


class AddNewReserveTime(APIView):
    permission_classes = [IsDoctor, ]

    def post(self, request):
        format = "%Y-%m-%dT%H:%M:%S%z"
        start_date = datetime.strptime(request.data['start_date'], format)
        end_date = datetime.strptime(request.data['end_date'], format)
        count = request.data['count']
        chunk = (end_date - start_date) / count
        visittime_objects = []
        visits = []
        try:
            for i in range(count):
                start = start_date + chunk * i
                end = start_date + chunk * (i + 1)
                visits.append((start, end))
                visittime_objects.append(VisitTime(start_date=start, end_date=end, doctor=request.user))
            VisitTime.objects.bulk_create(visittime_objects)

            return Response({'message': 'زمان رزرو اضافه شد'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': 'شما قادر به انجام این کار نیستید'}, status=status.HTTP_400_BAD_REQUEST)
