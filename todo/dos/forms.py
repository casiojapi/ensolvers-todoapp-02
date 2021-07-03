from django import forms
from django.forms import ModelForm

from .models import *


class DoForm(forms.ModelForm):
    
    class Meta:
        model = Do
        fields = '__all__'