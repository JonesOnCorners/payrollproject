from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Employee, Payroll
import xlwt
import time

# Create your views here.


def downloadreport(request):
    response = HttpResponse(content_type = 'application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="payroll.xls"'

    wb = xlwt.Workbook(encoding = 'utf-8')
    ws = wb.add_sheet('Payroll')

    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    
    columns = ['Employee Id','Employee Name','Payroll Month','Working Hours','Hourly Rate','Allowance','Deductions','Total Salary']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    
    font_style = xlwt.XFStyle()


    col_num = 0
    #rows = Payroll.objects.select_related('employee_id').values_list('employee_id','payroll_month','allowance','deductions','total_salary')
    rows = Payroll.objects.select_related('employee_id')
    counts = Payroll.objects.select_related('employee_id').count()
    print(counts)
    for x in rows:
        row_num +=1
        employee_id   = x.employee_id.employee_id
        employee_name = x.employee_id.employee_name
        #payroll_momth = time.strftime("%Y-%m-%d %H:%M",x.payroll_month)
        payroll_momth = 'May-2020'
        working_hours = x.employee_id.working_hours
        hourly_rate   = x.employee_id.hourly_rate
        allowance     = x.allowance
        deductions    = x.deductions
        total_salary  = x.total_salary
        ws.write(row_num, 0, employee_id, font_style)   
        ws.write(row_num, 1, employee_name, font_style) 
        ws.write(row_num, 2, payroll_momth, font_style) 
        ws.write(row_num, 3, working_hours, font_style) 
        ws.write(row_num, 4, hourly_rate, font_style)   
        ws.write(row_num, 5, allowance, font_style)     
        ws.write(row_num, 6, deductions, font_style)    
        ws.write(row_num, 7, total_salary, font_style)  
           
    # for row in rows:
    #      row_num += 1
    #      for col_num in range(len(row)):
    #          print(row)
    #          print(row[col_num])
             #ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

    

def insert_employee_payroll_data(employee_id
                                ,payroll_id
                                ,employee_name 
                                ,working_hours 
                                ,hourly_rate
                                ,is_admin      
                                ,created_by
                                ,updated_by    
                                ,active
                                ,allownance    
                                ,deductions
                                ,total_salary,
                                edit_insert 
                                 ):    

  
    if edit_insert == 'insert':
        try:
            print("INSIDE INSERT")
            e = Employee.objects.create(employee_name = employee_name,
                                    working_hours = working_hours,
                                    hourly_rate   = hourly_rate,
                                    is_admin      = is_admin,
                                    created_by    = created_by,
                                    updated_by    = updated_by,
                                    active        = active)
        
            print(e)
            p1 = Payroll()
            p1.employee_id = Employee.objects.get(employee_id = e.employee_id)
            p = Payroll.objects.create( employee_id   = p1.employee_id ,
                                        allowance     = allownance,
                                        deductions    = deductions,
                                        total_salary  = total_salary)
            print(p)
            return True
        except Exception:
            return False
    else:
        try:
            e = Employee.objects.get(employee_id = employee_id)
            e.employee_name = employee_name
            e.working_hours = working_hours
            e.hourly_rate = hourly_rate
            e.is_admin = is_admin
            e.created_by = created_by
            e.updated_by = updated_by
            e.save()
            p = Payroll.objects.get(payroll_id = payroll_id)
            p.allownance   = allownance
            p.deductions   = deductions
            p.total_salary = total_salary
            p.save()
            return True
        except Exception:
            return False
                                



def calculate_salary(working_hours, hourly_rate):
    """
    This function calculates the total monthly salary of an employee based on
    the working_hours and hourly_rate as (working_hours*hourly_rate)- standard_deduction
    Input  : Integers working_hours and hourly_rate
    Output : Total monthly salary
    """
    allownance    =  working_hours * hourly_rate
    deductions    =  allownance * 0.1
    total_salary  = allownance - deductions
    salary_list   = [int(allownance), int(deductions), int(total_salary)]
    return salary_list
    #return(int(allownance - deductions))


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

def deleteemployee(request):    
    try:
        e = Employee.objects.get(employee_id = request.GET.get('employee_id'))
        e.delete()
        employee_list = Payroll.objects.select_related('employee_id')                  
        return render(request, 'index.html',{'employee_list' : employee_list })
    except Exception:
        return render(request, 'error.html',{'error':'Delete Operation Failed'})


def editemployee(request):
    if request.method == 'POST':
        print("INSIDE EDIT")
        employee_id = request.POST.get("employee_id")
        print(employee_id)
        payroll_id = request.POST.get("payroll_id")
        print(payroll_id)
        employee_name = request.POST.get("employee_name")
        working_hours = request.POST.get("working_hours")
        hourly_rate   = request.POST.get("hourly_rate")
        is_admin      = request.POST.get("is_admin")
        created_by    = request.POST.get("created_by")        
        created_date  = request.POST.get("created_date")
        #updated_by    = request.GET.get("updated_by")
        updated_by    = request.user.username
        print(updated_by)
        updated_date  = request.POST.get("updated_date")
        active        = request.POST.get("active")
        
        salary_details  =  calculate_salary(int(working_hours), int(hourly_rate))
        
        is_updated = insert_employee_payroll_data(employee_id,
                                     payroll_id,
                                     employee_name, 
                                     working_hours, 
                                     hourly_rate,
                                     is_admin, 
                                     created_by, 
                                     updated_by, 
                                     active,
                                     salary_details[0],
                                     salary_details[1],
                                     salary_details[2],
                                     'edit'
                                     )
        if (is_updated): 
            print("RETURNING BECAUSE UPDATE COMPLETED")      
            employee_list = Payroll.objects.select_related('employee_id')                  
            return render(request, 'index',{'employee_list' : employee_list })
        else:
            return render(request,'error.html',{'error':'Update Failed'})    
    else: 
        employee_id = request.GET.get('employee_id')
        employee_list = Payroll.objects.select_related('employee_id').filter(employee_id = employee_id)
        return render(request,'editemployee.html',{'employee_list':employee_list})


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
        created_date  = request.POST.get("created_date")
        updated_by    = request.POST.get("updated_by")
        updated_date  = request.POST.get("updated_date")
        active        = request.POST.get("active")
       
        salary_details  =  calculate_salary(int(working_hours), int(hourly_rate))

        print(checkisadmin(created_by)) 
        if (not checkisadmin(created_by)):
            return render(request,'error.html',{'error':'Not an admin, cannot add employee'})
        
        #retireiving the employee_id to pass to payroll foreign key

        is_updated = insert_employee_payroll_data('',
                                    '',
                                    employee_name, 
                                    working_hours, 
                                    hourly_rate,
                                    is_admin, 
                                    created_by, 
                                    updated_by, 
                                    active,
                                    salary_details[0],
                                    salary_details[1],
                                    salary_details[2],
                                    'insert'                                                                         
                                     )
        if (is_updated):                         
            employee_list = Payroll.objects.select_related('employee_id')
            return render(request, 'index.html',{'employee_list' : employee_list })   
        else:
            return render(request,'error.html',{'error':'Insert Failed'})
                
    message = "Hello"
    return render(request,'addemployee.html',{'message':message})