from django.contrib.sites.shortcuts import get_current_site
from rest_framework import generics

from account.models import Account
from account.serializers import (
    AccountRegistrationSerializer,
)


class RegisterView(generics.CreateAPIView):
    queryset = Account.objects.all()
    permission_classes = ()
    serializer_class = AccountRegistrationSerializer

    def get_serializer_context(self):
        ctx = super(RegisterView, self).get_serializer_context()
        data = {
            'domain': 'http://' + get_current_site(self.request).domain,
        }
        ctx.update(data=data)
        return ctx
