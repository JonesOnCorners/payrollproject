# Generated by Django 2.2.12 on 2020-05-24 02:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payrollprocess', '0023_auto_20200523_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 5, 23, 22, 54, 31, 797883)),
        ),
        migrations.AlterField(
            model_name='employee',
            name='updated_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 5, 23, 22, 54, 31, 797883)),
        ),
        migrations.AlterField(
            model_name='payroll',
            name='payroll_month',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 5, 23, 22, 54, 31, 827915)),
        ),
    ]
