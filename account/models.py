from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from simple_history.models import HistoricalRecords

from _helpers.db import TimeModel


# Create your models here.

class AccountUserManager(BaseUserManager):
    def create_user(self, phone, email, password, **extra_fields):
        if not phone:
            raise ValueError('The phone must be set')
        if not email:
            raise ValueError('The email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, phone=phone, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(phone, email, password, **extra_fields)


class Account(AbstractUser, TimeModel):
    EXPERT = 'expert'
    PATIENT = 'patient'
    ROLES_CHOICES = (
        (EXPERT, 'متخصص'),
        (PATIENT, "بیمار")
    )
    ROLES_KINDS = tuple(dict(ROLES_CHOICES).keys())

    history = HistoricalRecords()
    username = None
    first_name = models.CharField(max_length=100, verbose_name='نام')
    last_name = models.CharField(max_length=100, verbose_name='نام خانوادگی')
    phone = models.CharField(
        verbose_name="شماره موبایل",
        validators=[RegexValidator(regex="^(09)[0-9]{9}$")],
        max_length=16,
        unique=True,
        db_index=True

    )
    email = models.EmailField(verbose_name="آدرس ایمیل", unique=True, db_index=True)
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['email', ]
    role = models.CharField(max_length=100,
                            choices=ROLES_CHOICES,
                            default='patient', verbose_name="نوع کاربر")

    objects = AccountUserManager()

    def __str__(self):
        if self.first_name is None or self.last_name is None:
            return self.email
        else:
            return self.first_name + " " + self.last_name

    class Meta:
        verbose_name = 'اکانت'
        verbose_name_plural = 'اکانت‌ها'
