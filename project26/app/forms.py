from django import forms
from app.models import User

class UserForm(forms.ModelForm):
    pwd=forms.CharField(max_length=15,widget=forms.PasswordInput)
    class Meta:
        model=User
        fields="__all__"