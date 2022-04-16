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


class FreeDietTemplatePart(models.Model):
    SATURDAY = 'saturday'
    SUNDAY = 'sunday'
    MONDAY = 'monday'
    TUESDAY = 'tuesday'
    WEDNESDAY = 'wednesday'
    THURSDAY = 'thursday'
    FRIDAY = 'friday'
    WEEKDAY_CHOICES = (
        (SATURDAY, 'شنبه'),
        (SUNDAY, 'یکشنبه'),
        (MONDAY, 'دوشنبه'),
        (TUESDAY, 'سه‌شنبه'),
        (WEDNESDAY, 'چهارشنبه'),
        (THURSDAY, 'پنج‌شنبه'),
        (FRIDAY, 'جمعه')
    )

    BREAKFAST = 'breakfast'
    LUNCH = 'lunch'
    DINNER = 'dinner'
    DIET_CHOICES = (
        (BREAKFAST, 'صبحانه'),
        (LUNCH, 'ناهار'),
        (DINNER, 'شام')
    )

    DIET_KINDS = tuple(dict(DIET_CHOICES).keys())
    WEEKDAY_KINDS = tuple(dict(WEEKDAY_CHOICES).keys())
    context = models.CharField(max_length=100, verbose_name='محتوا')
    meal = models.CharField(max_length=100, choices=DIET_CHOICES, verbose_name='وعده غذایی')
    week_day = models.CharField(max_length=100, verbose_name='روز هفته', choices=WEEKDAY_CHOICES)
    free_diet = models.ForeignKey(to=FreeDiet, on_delete=models.CASCADE, null=True, blank=True)

