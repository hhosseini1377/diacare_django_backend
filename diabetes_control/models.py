from django.db import models

from account.models import Account
from free_diet.models import FreeDiet

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
                            choices=VISIT_CHOICES, verbose_name='نوع ویزیت', default=DIABETES_CONTROL)

    def __str__(self):
        return "دکتر: " + self.doctor.__str__() + " / " + "بیمار: " + self.patient.__str__()

    class Meta:
        verbose_name = 'ویزیت'
        verbose_name_plural = 'ویزیت‌ها'


class SpecializedDiet(models.Model):
    name = models.CharField(max_length=50, verbose_name='نام رژیم', blank=True)
    visit = models.OneToOneField(VisitTime, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'رژیم غذایی'
        verbose_name_plural = "رژیم‌های غذایی"

    def __str__(self):
        return "برنامه رژیم توسط دکتر " + self.visit.doctor.last_name.__str__() + " برای بیمار: " + \
               self.visit.patient.__str__()


class DietTemplatePart(models.Model):
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
    free_diet = models.ForeignKey(to=FreeDiet, on_delete=models.CASCADE, null=True, blank= True)
    specialized_diet = models.ForeignKey(to=SpecializedDiet, on_delete=models.CASCADE, null=True, blank=True)
    # owner = models.ForeignKey(to=Account, on_delete=models.CASCADE, verbose_name='سازنده قطعه رژیم')

    def __str__(self):
        return self.week_day + "/" + self.meal + ': ' + self.context[:30]

    class Meta:
        verbose_name = 'بخش تمپلیت رژیم'
        verbose_name_plural = 'بخش‌های تمپلیت رژیم'


#
# class Template(models.Model):
#     name = models.CharField(max_length=100, verbose_name='نام تمپلیت')
#     owner = models.ForeignKey(to=Account, on_delete=models.CASCADE, verbose_name='سازنده تمپلیت رژیم')
#     template_parts = models.ManyToManyField(DietTemplatePart, verbose_name='بخش‌های تمپلیت')
#
#     class Meta:
#         verbose_name = 'تمپلیت رژیم'
#         verbose_name_plural = 'تمپلیت‌های رژیم'
#
#     def __str__(self):
#         return "برنامه رژیم توسط دکتر " + self.owner.__str__() + ":\n " + self.name


class Prescription(models.Model):
    context = models.CharField(max_length=1000, verbose_name='محتوا')
    visit = models.OneToOneField(VisitTime, on_delete=models.CASCADE, verbose_name='ویزیت')

    def __str__(self):
        return str('پزشک: ') + str(self.visit.doctor.__str__()) + " / " + str('بیمار: ') + str(
            self.visit.patient.__str__())

    class Meta:
        verbose_name = 'نسخه'
        verbose_name_plural = 'نسخه‌ها'
