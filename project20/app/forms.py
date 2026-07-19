from django import forms 
from app.models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields="__all__"

class RegisterForm(forms.Form):
    name=forms.CharField(max_length=20)
    uname=forms.CharField(max_length=20)
    password=forms.CharField(max_length=15,widget=forms.PasswordInput())