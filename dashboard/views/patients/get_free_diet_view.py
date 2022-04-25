from rest_framework.generics import RetrieveAPIView

from _helpers.custom_permisions import IsPatient
from dashboard.serializers.patients import FreeDietInstanceSerializer
from free_diet.models import FreeDietInstance


class GetFreeDietView(RetrieveAPIView):
    permission_classes = (IsPatient,)
    serializer_class = FreeDietInstanceSerializer

    def get_queryset(self):
        _q = FreeDietInstance.objects.filter(account=self.request.user)
        return _q
