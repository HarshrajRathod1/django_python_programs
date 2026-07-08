from django import forms
from django.core.validators import MinValueValidator

def name_validator(name):
    if not name.isalpha():
        raise forms.ValidationError(message="name must contain alphates only")
    return name

def job_validator(job):
    if not job in ["manager","acc","hr"]:
        raise forms.ValidationError(message="job must be manager acc or hr only")
    return job

class job_class_validator():
    def __call__(self,job):
        if not job in ["manager","acc","hr"]:
            raise forms.ValidationError(message="job must be manager acc or hr only")
        return job


class EmployeeForm(forms.Form):
    eno=forms.IntegerField(validators=[MinValueValidator(0)])
    name=forms.CharField(max_length=20,validators=[name_validator])
    job=forms.CharField(max_length=15,validators=[job_class_validator()]) 
    salary=forms.FloatField(validators=[MinValueValidator(1)])