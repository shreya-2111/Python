from django.shortcuts import render, redirect
from .models import Note

#Read
def note_list(request):
    notes = Note.objects.all().order_by('-created_at')
    return render(request,'notes/list.html',{'notes': notes})

#CREATE
def add_note(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Note.objects.create(title=title,content=content)
        return redirect('note_list')
    return render(request,'notes/add.html')

#UPDATE
def update_note(request,id):
    note = Note.objects.get(id=id)
    if request.method == 'POST':
        note.title = request.POST['title']
        note.content = request.POST['content']
        note.save()
        return redirect('note_list')
    return render(request,'notes/update.html',{'note': note})

#DELETE
def delete_note(request,id):
    note = Note.objects.get(id=id)
    note.delete()
    return redirect('note_list')

