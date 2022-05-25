from .models import Task
from django.forms import ModelForm, TextInput

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "deadtime"]
        widgets = {
            "title": TextInput(attrs={
            "class": "form-control",
            "id": "exampleInputEmail1",
            "aria-describedby": "emailHelp"
            }),
            "description": TextInput(attrs={
                "class": "form-control",
                "id": "exampleInputEmail1",
                "aria-describedby": "emailHelp"
            }),
            "deadtime": TextInput(attrs={
                "class": "form-control",
                "id": "exampleInputEmail1",
                "aria-describedby": "emailHelp"
            })
        }