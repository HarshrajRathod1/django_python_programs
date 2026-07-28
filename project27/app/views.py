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
    response=render(request,"login_temp.html",context={'form':form})
    return response
def logoutview(request):
    logout(request)
    response=redirect("login")
    return response
