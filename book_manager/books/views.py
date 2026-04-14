from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm

#READ
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/list.html',{'books': books})

#CREATE
def add_book(request):
    form = BookForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render (request, 'books/form.html',{'form': form})

#UPDATE
def update_book(request,id):
    book = Book.objects.get(id=id)
    form = BookForm(request.POST or None, instance=book)

    if form.is_valid():
        form.save()
        return redirect('book_list')
    
    return render(request, 'books/form.html',{'form': form})

#DELETE
def delete_book(request,id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('book_list')