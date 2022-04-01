from django.core.mail import EmailMessage
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from diacare_django_backend.settings import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD
from django.db.models import Q
from account.models import Account


class Util:
    @staticmethod
    def send_email(data):
        email = EmailMessage(subject=data['subject'], body=data['body'], to=[data['user_email']],
                             from_email=EMAIL_HOST_USER,)
        email.send()

    class CustomAuthenticationBackend(BaseBackend):
        def authenticate(self, request, email_or_phone=None, password=None):
            try:
                user = Account.objects.get(
                    Q(email=email_or_phone) | Q(phone=email_or_phone)
                )
                pwd_valid = user.check_password(password)
                if pwd_valid:
                    return user
                return None
            except Account.DoesNotExist:
                return None

        def get_user(self, user_id):
            try:
                return Account.objects.get(pk=user_id)
            except Account.DoesNotExist:
                return None
