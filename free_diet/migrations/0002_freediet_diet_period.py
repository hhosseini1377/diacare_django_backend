# Generated by Django 4.0.3 on 2022-04-08 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('free_diet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='freediet',
            name='diet_period',
            field=models.CharField(choices=[('onemonth', 'یک ماهه'), ('twomonth', 'دو ماهه'), ('threemonth', 'سه ماهه')], default='onemonth', max_length=100, verbose_name='مدت رژیم'),
        ),
    ]