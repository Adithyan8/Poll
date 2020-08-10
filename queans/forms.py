from django import forms
from .models import Question

class QuestionForm(forms.Form):
    pollq = forms.CharField(max_length=100)