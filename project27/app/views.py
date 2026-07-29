from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.http import HttpResponse
# Create your views here.

def user_register(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            response =redirect("login")
            return response
        else:
            return render(request,"register_temp.html",context={'form':form})
    form=UserCreationForm()
    response=render(request,"register_temp.html",context={'form':form})
    return response

def loginview(request):
    form=AuthenticationForm()
    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            response=render(request,"dashboard_temp.html")
            return response
        else:
            return render(request,"login_temp.html",context={'form':form})
    response=render(request,"login_temp.html",context={'form':form})
    return response


from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def dashboardview(request):
    response=render(request,"dashboard_temp.html")
    return response

@login_required(login_url='/login/')
def logoutview(request):
    logout(request)
    response=redirect("login")
    return response

from django.contrib.auth.forms import PasswordChangeForm

@login_required(login_url='/login/')
def passwordchange_view(request):
    if request.method=='POST':
        form=PasswordChangeForm(request.user,data=request.POST)
        if form.is_valid():
            form.save()
            logout(request)
            return redirect("login")
        else:
            return render(request,"password_change_temp.html",context={'form':form})
    form=PasswordChangeForm(request.user)
    response=render(request,"password_change_temp.html",context={'form':form})
    return response