from django.shortcuts import render, redirect
from .models import Student

#READ
def student_list(request):
    student = Student.objects.all()
    return render(request,'students/list.html',{'students': student })

#CREATE
def add_student(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        course = request.POST['course']

        Student.objects.create(name=name, email=email,course=course)
        return redirect('student_list')
    return render(request,'students/add.html')

#UPDATE
def update_student(request,id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        student.name = request.POST['name']
        student.email = request.POST['email']
        student.course = request.POST['course']
        student.save()
        return redirect('student_list')
    return render(request,'students/update.html',{'student': student }) 

#DELETE
def delete_student(request,id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('student_list')