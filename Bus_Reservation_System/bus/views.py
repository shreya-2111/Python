from django.shortcuts import render, redirect
from .models import Bus
from .forms import BusForm

# READ
def bus_list(request):
    buses = Bus.objects.all()
    return render(request, 'bus/list.html', {'buses': buses})

# CREATE
def add_bus(request):
    form = BusForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('bus_list')
    return render(request, 'bus/form.html', {'form': form})

# UPDATE
def update_bus(request, id):
    bus = Bus.objects.get(id=id)
    form = BusForm(request.POST or None, instance=bus)
    if form.is_valid():
        form.save()
        return redirect('bus_list')
    return render(request, 'bus/form.html', {'form': form})

# DELETE
def delete_bus(request, id):
    Bus.objects.get(id=id).delete()
    return redirect('bus_list')