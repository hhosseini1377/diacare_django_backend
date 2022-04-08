# Generated by Django 4.0.3 on 2022-04-08 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diabetes_control', '0004_dietkind_rename_diet_specializeddiet_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='freediet',
            name='kind',
        ),
        migrations.AddField(
            model_name='freediet',
            name='free_diet_kind',
            field=models.CharField(choices=[('weightgain', 'افزایش وزن'), ('weightloss', 'کاهش وزن')], default='weightloss', max_length=100, verbose_name='نوع رژیم'),
        ),
        migrations.DeleteModel(
            name='DietKind',
        ),
    ]