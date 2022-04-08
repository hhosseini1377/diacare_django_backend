from django.db import models
from account.models import Account


class FreeDiet(models.Model):

    WEIGHTGAIN = 'weightgain'
    WEIGHTLOSS = 'weightloss'
    FREEDIET_CHOICES = (
        (WEIGHTGAIN, 'افزایش وزن'),
        (WEIGHTLOSS, 'کاهش وزن'),
    )

    ONEMONTH = 'onemonth'
    TWOMONTH = 'twomonth'
    THREEMONTH = 'threemonth'
    PERIOD_CHOICES = (
        (ONEMONTH, 'یک ماهه'),
        (TWOMONTH, 'دو ماهه'),
        (THREEMONTH, 'سه ماهه'),
    )

    name = models.CharField(max_length=50, verbose_name='نام رژیم', blank=True)
    accounts = models.ManyToManyField(to=Account, related_name='diet_accounts')
    free_diet_kind = models.CharField(max_length=100, verbose_name='نوع رژیم', choices=FREEDIET_CHOICES, default=WEIGHTLOSS)
    diet_period = models.CharField(max_length=100, verbose_name='مدت رژیم', choices=PERIOD_CHOICES, default=ONEMONTH)
