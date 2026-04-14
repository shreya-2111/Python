from django.shortcuts import render
from .models import Product

def product_list(request):
    category = request.GET.get('category')

    if category:
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()

    return render(request, 'product_list.html', {
        'products': products
    })