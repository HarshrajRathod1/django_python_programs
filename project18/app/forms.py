from django import forms
from .models import UserRegister
class UserRegisterForm(forms.ModelForm):
    password=forms.CharField(max_length=20,widget=forms.PasswordInput())
    class Meta:
        model=UserRegister
        fields="__all__"