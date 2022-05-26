from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()


class AccountUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'avatar', 'optional_information']
        read_only_fields = ['pk', 'email', 'phone']
        extra_kwargs = {
            'password': {'write_only': True}
        }
