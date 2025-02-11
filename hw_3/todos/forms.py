from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    due_date = forms.DateField()
    class Meta:
        model = Todo
        fields = ['title', 'description', 'due_date', 'status']
