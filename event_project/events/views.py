from django.shortcuts import render, redirect
from .models import Event
from django import forms

# Form
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

# Show all events
def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})

# Add event
def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'add_event.html', {'form': form})