from django import forms
from .models import *

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        exclude = ['user']