from django.shortcuts import render, redirect
from .models import Admission
from .forms import AdmissionForm

# READ
def student_list(request):
    students = Admission.objects.all()
    return render(request, 'college/list.html', {'students': students})

# CREATE
def add_student(request):
    form = AdmissionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'college/form.html', {'form': form})

# UPDATE
def update_student(request, id):
    student = Admission.objects.get(id=id)
    form = AdmissionForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'college/form.html', {'form': form})

# DELETE
def delete_student(request, id):
    Admission.objects.get(id=id).delete()
    return redirect('student_list')