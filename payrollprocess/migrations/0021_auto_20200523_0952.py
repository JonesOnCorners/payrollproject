# Generated by Django 2.2.12 on 2020-05-23 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payrollprocess', '0020_auto_20200523_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='created_date',
            field=models.DateTimeField(blank=True, default='2020-May'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='updated_date',
            field=models.DateTimeField(blank=True, default='2020-May'),
        ),
        migrations.AlterField(
            model_name='payroll',
            name='payroll_month',
            field=models.DateTimeField(blank=True, default='2020-May'),
        ),
    ]
