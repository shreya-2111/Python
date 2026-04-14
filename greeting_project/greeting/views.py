from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


def greet(request):
    name = request.POST.get('name')
    return render(request, 'greet.html', {'name': name})