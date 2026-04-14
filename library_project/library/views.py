from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Book

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        User.objects.create_user(username=username, password=password)
        return redirect('login')

    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            request.session['username'] = username
            return redirect('dashboard')

    return render(request, 'login.html')

def dashboard(request):
    username = request.session.get('username')
    return render(request, 'dashboard.html', {'username': username})

def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        price = request.POST['price']

        Book.objects.create(title=title, author=author, price=price)
        return redirect('book_list')

    return render(request, 'add_book.html')

def book_list(request):
    books = Book.objects.all()

    # Filtering example
    search = request.GET.get('search')
    if search:
        books = Book.objects.filter(title__icontains=search)

    return render(request, 'book_list.html', {'books': books})