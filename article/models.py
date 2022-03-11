from django.db import models
from account.models import Account
# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=100)


class Article(models.Model):
    subject = models.CharField(max_length=100, verbose_name='subject', blank=False, null=False)
    context = models.CharField(max_length=10000, verbose_name='context', blank=False, null=False)
    writer = models.ForeignKey(Account, on_delete=models.CASCADE)
    thumbnail = models.ImageField(default='images/default.png')
    tag = models.ManyToManyField(Tag)
