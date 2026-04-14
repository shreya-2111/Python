from django.shortcuts import render
from .models import Job

def job_list(request):

    category = request.GET.get('category')

    if category:
        jobs = Job.objects.filter(category=category)
    else:
        jobs = Job.objects.all()

    return render(request, 'jobs/job_list.html', {'jobs': jobs})