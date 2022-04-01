from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.urls import reverse
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.tokens import RefreshToken

from account.models import Account
from account.utils import Util

User = get_user_model()


class AccountRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=Account.objects.all())]
    )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('email', 'phone', 'role', 'password', 'password2', 'first_name', 'last_name')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        print(validated_data['password'])
        user = User.objects.create(
            phone=validated_data['phone'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            role=validated_data['role']
        )
        user.set_password(validated_data['password'])
        user.save()
        token = RefreshToken.for_user(user=user)
        token['pass'] = validated_data['password']
        self.update_payload(token, user)
        abs_url = self.context['data'].get('domain') + reverse('verify-email') + "?token=" + str(token)
        self.send_email(abs_url, user)
        return user

    @staticmethod
    def send_email(abs_url, account):
        email_body = 'Hi ' + account.email + ' Use Link below to verify your email: \n' + abs_url
        email_data = {'body': email_body, 'subject': 'Verify your email', 'user_email': account.email}
        Util.send_email(data=email_data)

    @staticmethod
    def update_payload(token, user):
        token['email'] = user.email
        token['phone'] = user.phone
        token['role'] = user.role
