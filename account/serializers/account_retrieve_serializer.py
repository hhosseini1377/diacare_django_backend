import base64

from django.core.files import File
from rest_framework import serializers

from account.models import Account


class AccountRetrieveSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()

    class Meta:
        model = Account
        fields = ['pk', 'avatar', 'email', 'is_staff', 'phone', 'first_name', 'last_name', 'is_active',
                  'optional_information']

    def get_avatar(self, obj):
        f = open(obj.avatar.path, 'rb')
        image = File(f)
        data = base64.b64encode(image.read())
        return data
