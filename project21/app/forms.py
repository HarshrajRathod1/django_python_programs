from django import forms 
from app.models import Customer

class CustomerForm(forms.ModelForm):
    email=forms.CharField(max_length=20,widget=forms.EmailInput())
    class Meta:
        model=Customer
        fields="__all__"