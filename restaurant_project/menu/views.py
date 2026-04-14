from django.shortcuts import render,redirect
from .models import Food

def food_list(request):

    category = request.GET.get('category')

    if category:
        foods = Food.objects.filter(category=category)
    else:
        foods = Food.objects.all()

    return render(request, 'menu/food_list.html', {'foods': foods})

def add_food(request):

    if request.method == "POST":
        name = request.POST['name']
        price = request.POST['price']
        category = request.POST['category']
        description = request.POST['description']

        Food.objects.create(
            name=name,
            price=price,
            category=category,
            description=description
        )

        return redirect('food_list')

    return render(request, 'menu/add_food.html')