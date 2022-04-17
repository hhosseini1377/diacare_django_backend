from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from free_diet.models import FreeDiet, FreeDietTemplatePart


# Create your views here.


class FreeDietView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            kind, period, weight, height = request.data['kind'], request.data['period'], request.data['weight'], \
                                           request.data['height']
        except Exception as e:
            return Response({'message': 'موارد کامل وارد نشده است'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            suggested_free_diet = FreeDiet.objects.filter(free_diet_kind=kind, diet_period=period)[0]
        except Exception as e:
            return Response({'message': 'رژیمی با اطلاعات وارد شده وجود ندارد'}, status=status.HTTP_400_BAD_REQUEST)

        diet_templates = FreeDietTemplatePart.objects.filter(free_diet=suggested_free_diet).order_by('week_day')
        diet_part_response = []

        for diet_template in diet_templates:
            template = {'وعده': diet_template.meal, 'روز': diet_template.week_day, 'محتوا': diet_template.context}
            diet_part_response.append(template)

        response = {'نام رژیم': suggested_free_diet.name, 'محتوی رژیم': diet_part_response,
                    'id': suggested_free_diet.pk}
        return Response(response)
