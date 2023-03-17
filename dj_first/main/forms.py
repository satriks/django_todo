from .models import Task
from django.forms import ModelForm, TextInput, Textarea


class TaskForms(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task"]
        widgets = {'title': TextInput(attrs={
            'class': 'form-control',
            'placeholder': "Введите назвние"}),

            'task': Textarea(attrs={
            'class': 'form-control',
            'placeholder': "Введите описание"})

        }