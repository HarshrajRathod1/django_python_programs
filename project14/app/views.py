from django.shortcuts import render
from app.forms import RegisterForm
from app.models import RegisterUser
from django.http import HttpResponse
# Create your views here.
def register_view(request):
    msg=""
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            form=RegisterForm()
            msg="saved"
        else:
            response=render(request,"emp_temp.html",context={'form':form})
            return response
    form=RegisterForm()
    response=render(request,"emp_temp.html",context={'form':form,'msg':msg})
    return response


def update_register(request):
    msg=""
    if request.method=="POST":
        user=RegisterUser.objects.get(uname=request.POST.get("uname"))
        form=RegisterForm(instance=user,data=request.POST)
        if form.is_valid():
            form.save()
            response=HttpResponse("<h2>Updated</h2>")
            return response
        else:
            response=render(request,"update_reg_temp.html",context={'form':form})
            return response
    uname=request.GET.get('uname')
    user=RegisterUser.objects.get(uname=uname)
    form=RegisterForm(instance=user)
    response=render(request,"update_reg_temp.html",context={'form':form,'msg':msg})
    return response

from app.models import Employee
from app.forms import EmployeeForm
def update_emp(request):
    msg=""
    if request.method=="POST":
        emp=Employee.objects.get(empno=request.POST.get("empno"))
        emp_form=EmployeeForm(instance=emp,data=request.POST)
        if emp_form.is_valid():
            emp_form.save()
            msg="saved"
            emp_form=EmployeeForm()
            response=render(request,"update_emp_temp.html",context={'form':emp_form,'msg':msg})
            return response

        else:
            response=render(request,"update_emp_temp.html",context={'form':emp_form})
            return response 
    emp=Employee.objects.get(empno=request.GET.get("empno"))
    emp_form=EmployeeForm(instance=emp)
    response=render(request,"update_emp_temp.html",context={'form':emp_form,'msg':msg})
    return response
