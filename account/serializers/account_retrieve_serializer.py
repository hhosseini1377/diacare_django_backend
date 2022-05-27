import base64

from django.core.files import File
from rest_framework import serializers

from account.models import Account


class AccountRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['pk', 'avatar', 'email', 'is_staff', 'phone', 'first_name', 'last_name', 'is_active',
                  'optional_information']

