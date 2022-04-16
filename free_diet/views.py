from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FreeDiet
from diabetes_control.models import DietTemplatePart
from .models import FreeDietTemplatePart, FreeDietInstance
from rest_framework import status
from _helpers.custom_permisions import IsDoctor, IsPatient
from rest_framework import generics
from free_diet.serializers import AddFreeDietSerializer
# Create your views here.


class FreeDietView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            kind, period, weight, height = request.data['kind'], request.data['period'], request.data['weight'], request.data['height']
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

        response = {'نام رژیم': suggested_free_diet.name, 'محتوی رژیم': diet_part_response, 'id': suggested_free_diet.pk}
        return Response(response)


class AddFreeDiet(generics.CreateAPIView):
    permission_classes = [IsPatient, ]
    serializer_class = AddFreeDietSerializer
    # def post(self, request):
    #     try:
    #
    #         free_diet = FreeDiet.objects.get(pk=request.query_params['id'])
    #     except Exception as e:
    #         return Response({"message": "شناسه رژیم رایگان نامعتبر می‌باشد."}, status=status.HTTP_400_BAD_REQUEST)
    #
    #     free_diet.accounts.add(request.user)
    #     return Response({"message": "این رژیم به رژیم‌های رایگان شما اضافه شد."}, status=status.HTTP_200_OK)
    #
    #
