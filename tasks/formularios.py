from .models import Task
from django import forms


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["titulo", "ubicacion", "reseña"]
        widgets = {
            "titulo": forms.TextInput(
                attrs={"class": "form-control ", "placeholder": "Nombre del Hospital"}
            ),
            "ubicacion": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Escribe la ubicacion"}
            ),
            "reseña": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Escribe una reseña"}
            ),
        }
