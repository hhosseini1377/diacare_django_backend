# Generated by Django 4.0.3 on 2022-03-22 00:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_account_email_alter_account_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='created',
        ),
        migrations.RemoveField(
            model_name='account',
            name='modified',
        ),
        migrations.RemoveField(
            model_name='historicalaccount',
            name='created',
        ),
        migrations.RemoveField(
            model_name='historicalaccount',
            name='modified',
        ),
    ]
