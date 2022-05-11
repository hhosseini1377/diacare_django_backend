from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from _helpers.custom_permisions import IsDoctor
from diabetes_control.models import VisitTime
from diabetes_control.serializers import SpecializedDietSerializer


class AddSpecializedDietToVisitView(APIView):
    permission_classes = (IsDoctor,)
    serializer_class = SpecializedDietSerializer

    def post(self, request):
        visit = get_object_or_404(VisitTime, pk=request.data.get('visit', None))
        if visit.doctor != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'کاربر حق ایجاد تغییر در این رژیم را ندارد.'})
        data = {
            'visit': request.data.get('visit'),
            'name': request.data.get('نام رژیم'),
            'diet_parts': request.data.get('محتوی رژیم')
        }
        serializer = self.serializer_class(data=data, context={
            'request': request,
            'format': self.format_kwarg,
            'view': self
        })
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
