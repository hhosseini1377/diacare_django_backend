from django.contrib import admin
from django.db import models

from account.models import Account


# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'تگ'
        verbose_name_plural = 'تگ‌ها'


class Article(models.Model):
    subject = models.CharField(max_length=100, verbose_name='subject', blank=False, null=False)
    context = models.CharField(max_length=10000, verbose_name='context', blank=False, null=False)
    writer = models.ForeignKey(Account, on_delete=models.CASCADE)
    thumbnail = models.ImageField(default='default_avatar.png')
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.subject + ' by ' + self.writer.__str__()

    @admin.display(
        ordering='tags',
        description='tags'
    )
    def get_tags(self):
        return ", ".join([tag.name for tag in self.tags.all()])

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقاله‌ها'
