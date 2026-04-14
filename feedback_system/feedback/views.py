from django.shortcuts import render, redirect
from .models import Feedback
from .forms import FeedbackForm

#READ
def feedback_list(request):
    data = Feedback.objects.all()
    return render(request, 'feedback/list.html',{'data':data})

#CREATE 
def add_feedback(request):
    form = FeedbackForm()

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback_list')
    return render(request, 'feedback/add.html',{'form':form})
    
#UPDATE
def update_feedback(request,id):
    feedback = Feedback.objects.get(id=id)
    form = FeedbackForm(instance=feedback)

    if request.method == 'POST':
        form = FeedbackForm(request.POST, instance=feedback)
        if form.is_valid():
            form.save()
            return redirect ('feedback_list')
    return render(request, 'feedback/update.html',{'form':form})

#DELETE
def delete_feedback(request,id):
    Feedback.objects.get(id=id).delete()
    return redirect('feedback_list')