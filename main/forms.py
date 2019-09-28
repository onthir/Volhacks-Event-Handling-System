from django import forms
from .models import *

class AddEventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ['event_name', 'volunteers',]