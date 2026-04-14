from django.shortcuts import render, redirect
from .models import Employee

# READ
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/list.html', {'employees': employees})

# CREATE
def add_employee(request):
    if request.method == 'POST':
        Employee.objects.create(
            name=request.POST['name'],
            department=request.POST['department'],
            salary=request.POST['salary'],
            status='status' in request.POST
        )
        return redirect('employee_list')

    return render(request, 'employees/add.html')

# UPDATE
def update_employee(request, id):
    emp = Employee.objects.get(id=id)

    if request.method == 'POST':
        emp.name = request.POST['name']
        emp.department = request.POST['department']
        emp.salary = request.POST['salary']
        emp.status = 'status' in request.POST
        emp.save()
        return redirect('employee_list')

    return render(request, 'employees/update.html', {'emp': emp})

# DELETE
def delete_employee(request, id):
    Employee.objects.get(id=id).delete()
    return redirect('employee_list')