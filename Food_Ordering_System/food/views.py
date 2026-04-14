from django.shortcuts import render, redirect
from .models import FoodItem
from .forms import FoodForm

# READ
def menu_list(request):
    items = FoodItem.objects.all()
    return render(request, 'food/list.html', {'items': items})

# CREATE
def add_food(request):
    form = FoodForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('menu_list')
    return render(request, 'food/form.html', {'form': form})

# UPDATE
def update_food(request, id):
    item = FoodItem.objects.get(id=id)
    form = FoodForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('menu_list')
    return render(request, 'food/form.html', {'form': form})

# DELETE
def delete_food(request, id):
    FoodItem.objects.get(id=id).delete()
    return redirect('menu_list')

# ORDER
def order_food(request, id):
    return render(request, 'food/order.html', {'id': id})