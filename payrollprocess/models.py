from django.db import models
from datetime import datetime
#from djongo import models

# Create your models here.
class Employee(models.Model):
    employee_id     = models.AutoField(primary_key = True, max_length = 40)
    employee_name   = models.CharField(max_length = 255)
    #working_hours   = models.DecimalField(max_digits = 10, decimal_places = 1)
    working_hours   = models.IntegerField()
    hourly_rate     = models.IntegerField()
    is_admin        = models.CharField(max_length = 1, default  = 'N', blank = True, null = True)
    created_by      = models.CharField(max_length = 255)
    created_date    = models.DateTimeField(default = datetime.now(), blank = True)
    updated_by      = models.CharField(max_length = 255)
    updated_date    = models.DateTimeField(default = datetime.now(), blank = True) 
    active          = models.CharField(max_length = 1)    

    def __str__(self):
        return "%s %s %s %s %s" %(self.employee_id, self.employee_name, self.working_hours, self.hourly_rate, self.is_admin)

class Payroll(models.Model):
    payroll_id  = models.AutoField(primary_key = True, max_length = 40)
    employee_id = models.ForeignKey('Employee', on_delete=models.CASCADE)
    payroll_month = models.DateTimeField(default = datetime.now(), blank = True)
    allowance     = models.IntegerField()
    deductions    = models.IntegerField()
    total_salary  = models.IntegerField()

    def __str__(self):
        return "%s %s %s %s %s"%(self.payroll_id, self.payroll_month, self.allowance, self.deductions,self.total_salary)





    


                                