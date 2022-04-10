from rest_framework.generics import UpdateAPIView
from rest_framework.views import APIView
from _helpers.custom_permisions import IsPatient
from diabetes_control.models import VisitTime
from diabetes_control.serializers import VisitTimeUpdateSerializer
from rest_framework.response import Response
from rest_framework import status


class AddPatientToVisitView(APIView):
    permission_classes = (IsPatient,)
    serializer_class = VisitTimeUpdateSerializer

    def patch(self, request, pk):
        user = self.request.user
        object = self.get_object(pk)
        serializer = self.serializer_class(object, data={'patient': user.pk}, partial=True, context={
            'request': request,
            'format': self.format_kwarg,
            'view': self
        })

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def get_object(self, pk):
        return VisitTime.objects.get(pk=pk)
