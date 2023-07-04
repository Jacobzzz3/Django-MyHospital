from .models import Task
from django import forms


class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=['title','descripcion']
        widgets={
            'title': forms.TextInput(attrs={'class':'form-control ','placeholder':'Titulo de la tarea'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control','placeholder':'Titulo Descripcion'}),
        }
        