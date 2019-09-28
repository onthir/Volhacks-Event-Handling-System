from django import forms
from .models import *
from django.contrib.auth.models import User

class AddEventForm(forms.ModelForm):
    event_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    volunteers = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={'class':'form-control'}))
                                          
    class Meta:
        model = Event
        fields = ['event_name', 'volunteers',]