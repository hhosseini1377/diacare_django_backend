from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination

from _helpers.custom_permisions import IsPatient
from dashboard.serializers.patients import FreeDietInstanceAbstractSerializer
from free_diet.models import FreeDietInstance


class RetrieveListFreeDiets(ListAPIView):
    permission_classes = (IsPatient,)
    serializer_class = FreeDietInstanceAbstractSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        _q = FreeDietInstance.objects.filter(account=self.request.user)
        return _q
