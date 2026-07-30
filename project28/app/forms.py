from app.models import Student
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    role=forms.ChoiceField(choices=(('Admin','Admin'),('employees','employees')))
    class Meta:
        model=User
        fields=['username','password1','password2','role']