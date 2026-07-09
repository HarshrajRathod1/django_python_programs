from django import forms 
from app.models import RegisterUser
from app.models import Employee
class RegisterForm(forms.ModelForm):
    password=forms.CharField(max_length=15,widget=forms.PasswordInput())
    repassword=forms.CharField(max_length=15,widget=forms.PasswordInput())
    class Meta:
        model=RegisterUser
        #fields = ['name','uname','password'] 
        fields = "__all__" 

    def clean(self):
        cleaned_data=super().clean()
        if cleaned_data['password']!=cleaned_data['repassword']:
            raise forms.ValidationError(message="password and repassword must be same")
        return cleaned_data
    
class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields="__all__"