from django.shortcuts import render
from app.forms import Student
from django.http import HttpResponse
# Create your views here.

def student_view(request):
    if request.method=="POST":
        form=Student(request.POST)
        if form.is_valid():
            msg="FORM DATA SAVED!"
            response=HttpResponse(msg)
            return response
        else:
            response=render(request,"stud_temp.html",context={'form':form})
            return response
    form=Student()
    response=render(request,"stud_temp.html",context={'form':form})
    return response


def student1_view(request):
    if request.method=="POST":
        form=Student(request.POST)
        if form.is_valid():
            msg="FORM DATA SAVED! from student1"
            response=HttpResponse(msg)
            return response
        else:
            response=render(request,"stud1_temp.html",context={'form':form})
            return response
    form=Student()
    response=render(request,"stud1_temp.html",context={'form':form})
    return response

