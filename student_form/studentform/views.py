from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm

# READ
def student_list(request):
    students = Student.objects.all()
    return render(request, 'studentform/list.html', {'students': students})

# CREATE
def add_student(request):
    form = StudentForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('student_list')

    return render(request, 'studentform/form.html', {'form': form})

# UPDATE
def update_student(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(request.POST or None, instance=student)

    if form.is_valid():
        form.save()
        return redirect('student_list')

    return render(request, 'studentform/form.html', {'form': form})

# DELETE
def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('student_list')