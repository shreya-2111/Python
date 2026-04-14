from django.shortcuts import render, redirect
from .models import Patient
from .forms import PatientForm

# READ
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'hospital/list.html', {'patients': patients})

# CREATE
def add_patient(request):
    form = PatientForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('patient_list')

    return render(request, 'hospital/form.html', {'form': form})

# UPDATE
def update_patient(request, id):
    patient = Patient.objects.get(id=id)
    form = PatientForm(request.POST or None, instance=patient)

    if form.is_valid():
        form.save()
        return redirect('patient_list')

    return render(request, 'hospital/form.html', {'form': form})

# DELETE
def delete_patient(request, id):
    patient = Patient.objects.get(id=id)
    patient.delete()
    return redirect('patient_list')