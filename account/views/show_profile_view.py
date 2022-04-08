from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from account.serializers import AccountRetrieveSerializer

User = get_user_model()


class GetProfileView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = AccountRetrieveSerializer
