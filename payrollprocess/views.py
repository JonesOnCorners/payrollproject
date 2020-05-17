from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Employee, Payroll

# Create your views here.

def checkisadmin(employee_name):
    print(employee_name)
    isAdmin = Employee.objects.values('is_admin').filter(employee_name = employee_name)
    isActive = Employee.objects.values('active').filter(employee_name = employee_name)
    
    isAdminFlag  = 'N'
    isActiveFlag = 'N'

    for x in isAdmin:
        isAdminFlag = x['is_admin']
    
    for x in isActive:
        isActiveFlag = x['active']

    print(isActiveFlag+ ' '+ isAdminFlag)
    if isAdminFlag == 'N' or isActiveFlag == 'N' :
        return False
    else:
        return True

def index(request):
    #employee_list = Employee.objects.order_by('-employee_id')
    employee_list = Payroll.objects.select_related('employee_id')
    return render(request, 'index.html',{'employee_list' : employee_list })

def addemployee(request):
    if request.method == "POST":
        employee_name = request.POST.get("employee_name")
        working_hours = request.POST.get("working_hours")
        hourly_rate   = request.POST.get("hourly_rate")
        is_admin      = request.POST.get("is_admin")
        created_by    = request.POST.get("created_by")
        
        print(checkisadmin(created_by)) 

        if (not checkisadmin(created_by)):
            return render(request,'error.html',{'error':'Not an admin, cannot add employee'})

        created_date  = request.POST.get("created_date")
        updated_by    = request.POST.get("updated_by")
        updated_date  = request.POST.get("updated_date")
        active        = request.POST.get("active")

        allownance    =  int(working_hours) * int(hourly_rate)
        deductions    =  allownance * 0.1
        total_salary  =  allownance - deductions

        e = Employee.objects.create(employee_name = employee_name,
                                    working_hours = working_hours,
                                    hourly_rate   = hourly_rate,
                                    is_admin      = is_admin,
                                    created_by    = created_by,
                                    updated_by    = updated_by,
                                    active        = active)
        
        p1 = Payroll()
        p1.employee_id = Employee.objects.get(employee_id = e.employee_id)

        
        p = Payroll.objects.create( employee_id   = p1.employee_id ,
                                    allowance     = allownance,
                                    deductions    = deductions,
                                    total_salary  = total_salary
                                    )
        
    message = "Hello"
    return render(request,'addemployee.html',{'message':message})