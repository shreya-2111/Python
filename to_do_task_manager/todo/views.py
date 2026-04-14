from django.shortcuts import render, redirect
from .models import Task

# READ
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo/list.html', {'tasks': tasks})

# CREATE
def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']

        Task.objects.create(title=title, description=description)
        return redirect('task_list')

    return render(request, 'todo/add.html')

# UPDATE
def update_task(request, id):
    task = Task.objects.get(id=id)

    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.is_completed = 'is_completed' in request.POST
        task.save()

        return redirect('task_list')

    return render(request, 'todo/update.html', {'task': task})

# DELETE
def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('task_list')