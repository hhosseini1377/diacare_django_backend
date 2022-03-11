from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser

# Create your models here.

ROLES_CHOICES = (
    ("expert", "expert",
     "expert", "patient")
)


class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=100, verbose_name='first_name', blank=False, null=False)
    last_name = models.CharField(max_length=100, verbose_name='last_name', blank=False, null=False)
    phone_number = models.CharField(
        verbose_name="phone number",
        validators=[RegexValidator(regex="^(09)[0-9]{9}$")],
        max_length=16,
        unique=True,
    )
    email = models.EmailField(verbose_name="email address", null=True, blank=True, unique=True)
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']
    role = models.CharField(max_length=100,
                            choices=ROLES_CHOICES,
                            default='patient')

