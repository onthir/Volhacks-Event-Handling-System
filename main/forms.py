from django import forms
from .models import *
from django.contrib.auth.models import User

# add event form
class AddEventForm(forms.ModelForm):
    event_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
                                          
    class Meta:
        model = Event
        fields = ['event_name', ]

# task form

class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'completed',)