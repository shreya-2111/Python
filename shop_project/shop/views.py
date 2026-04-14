from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def filter_products(request):
    category = request.GET.get('category')
    products = Product.objects.filter(category=category)
    return render(request, 'product_list.html', {'products': products})