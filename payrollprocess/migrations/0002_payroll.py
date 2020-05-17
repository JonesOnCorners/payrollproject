# Generated by Django 2.2.12 on 2020-05-15 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payrollprocess', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payroll',
            fields=[
                ('payroll_id', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('payroll_month', models.DateField()),
                ('allowance', models.IntegerField()),
                ('deductions', models.IntegerField()),
                ('total_salary', models.IntegerField()),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payrollprocess.Employee')),
            ],
        ),
    ]
