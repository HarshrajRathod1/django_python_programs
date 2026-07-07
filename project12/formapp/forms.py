from django import forms
from django.core.validators import RegexValidator,EmailValidator,MinValueValidator,MaxValueValidator
class Person(forms.Form):
    name=forms.CharField(max_length=20,validators=[RegexValidator(r'[A-Za-z]{1,20}',"name must contain only alphabets")])
    age=forms.IntegerField(validators=[MinValueValidator(14),MaxValueValidator(100)]) 
    email=forms.CharField(max_length=20,validators=[EmailValidator]) 
    mobile=forms.CharField(max_length=10,validators=[RegexValidator(r'[0-9]{10}',"mobile number must contain 10 digits")]) 