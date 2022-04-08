from django.db import models
from account.models import Account


class FreeDiet(models.Model):

    WEIGHTGAIN = 'weightgain'
    WEIGHTLOSS = 'weightloss'
    FREEDIET_CHOICES = (
        (WEIGHTGAIN, 'افزایش وزن'),
        (WEIGHTLOSS, 'کاهش وزن'),
    )

    DIET_KINDS = tuple(dict(FREEDIET_CHOICES).keys())
    name = models.CharField(max_length=50, verbose_name='نام رژیم', blank=True)
    accounts = models.ManyToManyField(to=Account, related_name='diet_accounts')
    free_diet_kind = models.CharField(max_length=100, verbose_name='نوع رژیم', choices=FREEDIET_CHOICES, default=WEIGHTLOSS)

