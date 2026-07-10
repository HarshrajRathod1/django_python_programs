from django import forms 

def name(name):
    if name.isalpha():
        return name
    raise forms.ValidationError(message="name should alphabet only")

def course(course):
    if course in ["python","java","oracle"]:
        return course
    raise forms.ValidationError("Please select valid course python ,java or oracle") 

class Student(forms.Form):
    sno=forms.IntegerField(label="Student Number",required=True,help_text="Enter only digits")
    name=forms.CharField(max_length=20,label="Student Name",required=True,help_text="Enter alphabets only",validators=[name])
    course=forms.CharField(max_length=20,label="Student Course",required=True,help_text="Course must Python, Java or oracle",validators=[course])