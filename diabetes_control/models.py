from django.db import models

from account.models import Account


# Create your models here.


class VisitTime(models.Model):
    DIABETES_CONTROL = 'diabetes_control'
    SPECIAL_PROGRAM = 'specialized_program'
    VISIT_CHOICES = (
        (DIABETES_CONTROL, 'کنترل دیابت'),
        (SPECIAL_PROGRAM, 'برنامه مخصوص غذایی')

    )
    VISIT_KINDS = tuple(dict(VISIT_CHOICES).keys())

    start_date = models.DateTimeField(blank=False, null=False, verbose_name='شروع')
    end_date = models.DateTimeField(blank=False, null=False, verbose_name='پایان')
    doctor = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='doctor_visits', verbose_name='پزشک')
    patient = models.ForeignKey(Account, blank=True, null=True, on_delete=models.CASCADE, related_name='patient_visits',
                                verbose_name='بیمار')
    type = models.CharField(max_length=100,
                            choices=VISIT_CHOICES, verbose_name='نوع ویزیت')


class Diet(models.Model):
    visit = models.OneToOneField(VisitTime, on_delete=models.CASCADE)


class DietTemplate(models.Model):
    BREAKFAST = 'breakfast'
    LUNCH = 'lunch'
    DINNER = 'dinner'
    DIET_CHOICES = (
        (BREAKFAST, 'صبحانه'),
        (LUNCH, 'ناهار'),
        (DINNER, 'شام')
    )
    DIET_KINDS = tuple(dict(DIET_CHOICES).keys())

    context = models.CharField(max_length=100, verbose_name='محتوا')
    meal = models.CharField(max_length=100, choices=DIET_CHOICES, verbose_name='وعده غذایی')


class DietPart(models.Model):
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
    WEEKDAY_KINDS = tuple(dict(WEEKDAY_CHOICES).keys())
    week_day = models.CharField(max_length=100, verbose_name='روز هفته', choices=WEEKDAY_CHOICES)
    template = models.ForeignKey(to=DietTemplate, on_delete=models.CASCADE, related_name='diet_template',
                                 verbose_name='تمپلیت رژیم')
    diet = models.ForeignKey(to=Diet, on_delete=models.CASCADE, related_name='diet_parts', verbose_name='رژیم')

    def __str__(self):
        return str(self.diet.id) + " " + str(self.template.meal) + " " + str(self.week_day)


class Prescription(models.Model):
    context = models.CharField(max_length=1000, verbose_name='محتوا')
    visit = models.OneToOneField(VisitTime, on_delete=models.CASCADE, verbose_name='ویزیت')

    def __str__(self):
        return str('دکتر:') + str(self.visit.doctor) + "/" + str('بیمار:') + str(self.visit.patient)
