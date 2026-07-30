from django.shortcuts import render,redirect
from app.models import Student
from app.forms import UserRegistrationForm
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def register_view(request):
    if request.method=="POST":
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save()
            role=form.cleaned_data['role']
            group=Group.objects.get(name=role)
            user.groups.add(group)
            return redirect("login")
        else:
            return render(request,"register_temp.html",context={'form':form})
    form=UserRegistrationForm()
    return render(request,"register_temp.html",context={'form':form})

def login_view(request):
    msg=''
    if request.method=="POST":
        uname=request.POST.get("uname")
        pwd=request.POST.get("pwd")
        user=authenticate(request,username=uname,password=pwd)
        if user:
            login(request,user)
            return redirect("dashboard")
        else:
            msg="Invalid Username password"
            return render(request,"login_temp.html",context={'msg':msg})
    return render(request,"login_temp.html",context={'msg':msg})

@login_required(login_url="login")
def dashboard_view(request):
    user=request.user
    if user.groups.filter(name='Admin').exists():
        return render(request,"admin_dashboard_temp.html",context={'user':user})
    else:
        return render(request,"emp_dash_temp.html",context={'user':user})
@login_required(login_url="login")
def logout_view(request):
    user=request.session.flush()
    logout(user)
    return redirect("login")
