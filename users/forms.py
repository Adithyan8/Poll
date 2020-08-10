from django import forms
from .models import Creator
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    class meta:
        model = User
        fields=['__all__']