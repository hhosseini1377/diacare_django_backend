from _helpers.custom_permisions import IsPatient
from rest_framework import generics
from free_diet.serializers import AddFreeDietSerializer
from rest_framework import generics

from _helpers.custom_permisions import IsPatient
from free_diet.serializers import AddFreeDietSerializer


# Create your views here.


class AddFreeDiet(generics.CreateAPIView):
    permission_classes = [IsPatient, ]
    serializer_class = AddFreeDietSerializer
