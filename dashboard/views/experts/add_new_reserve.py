from diabetes_control.models import VisitTime
from rest_framework.views import APIView
from _helpers.custom_permisions import IsDoctor

from rest_framework.response import Response
from rest_framework import status


class AddNewReserveTime(APIView):
    permission_classes = [IsDoctor, ]

    def post(self, request):
        start_date = request.data['start_date']
        end_date = request.data['end_date']
        try:
            VisitTime.objects.create(start_date=start_date, end_date=end_date, doctor=request.user)
            return Response({'message': 'زمان رزرو اضافه شد'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': 'شما قادر به انجام این کار نیستید'}, status=status.HTTP_400_BAD_REQUEST)
