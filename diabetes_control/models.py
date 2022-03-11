from django.db import models
from account.models import Account
# Create your models here.

VISIT_CHOICES = (
    ('1', 'diabetes_control'),
    ('2', 'specialized_program')

)


class VisitTime(models.Model):
    start_date = models.DateTimeField(blank=False, null=False)
    end_date = models.DateTimeField(blank=False, null=False)
    doctor = models.ForeignKey(Account)
    patient = models.ForeignKey(blank=True, null=True)
    type = models.CharField(max_length=100,
                            choices=VISIT_CHOICES)


DIET_CHOICES = (
    ('1', 'breakfast'),
    ('2', 'lunch'),
    ('3', 'dinner')
)


class Diet(models.Model):
    visit = models.OneToOneField(VisitTime, on_delete=models.CASCADE)


class DietTemplate(models.Model):
    context = models.CharField(max_length=100)
    meal = models.CharField(max_length=100,
                            choices=DIET_CHOICES)


class DietPart(models.Model):
    # TODO: weekday choicefield
    week_day = models.CharField(max_length=100, )
    template = models.ForeignKey(to=DietTemplate, on_delete=models.CASCADE, related_name='diet_template')
    diet = models.ForeignKey(to=Diet, on_delete=models.CASCADE, related_name='diet_dietpart')


class Prescription(models.Model):
    context = models.CharField(max_length=1000)
    visit = models.OneToOneField(VisitTime, on_delete=models.CASCADE)





