from django.shortcuts import render
from app.forms import EmployeeForm
# Create your views here.

def emp_register(request):
    msg=""
    if request.method=="POST":
        form=EmployeeForm(request.POST)
        if form.is_valid():
            msg="form submited"
        else:
            response=render(request,"emp_temp.html",context={'form':form})
            return response 
    form=EmployeeForm()
    response=render(request,"emp_temp.html",context={'form':form,'msg':msg})
    return response