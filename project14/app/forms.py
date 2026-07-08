from django import forms 
from app.models import RegisterUser

class RegisterForm(forms.ModelForm):
    class Meta:
        model=RegisterUser
        fields = ['name','uname','password'] 
        #fields = "__all__" 