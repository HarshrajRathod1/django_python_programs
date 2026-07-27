from django.shortcuts import render,redirect
from app.models import User,Emails
from app.forms import UserForm
from django.urls import reverse_lazy
# Create your views here.

def login_home(request):
    form=UserForm()
    response=render(request,"login.html",context={'form':form})
    return response

def login(request):
    uname=request.GET.get('user')
    pwd=request.GET.get('pwd')
    try:
        User.objects.get(user=uname,pwd=pwd)
        request.session["uname"]=uname
        response=render(request,"inbox.html",context={'user':uname})
        return response
    except:
        form=UserForm()
        response=render(request,"login.html",context={'form':form,'msg':'Invalid UserName or Password'})
        return response

def allEmails(request):
    uname=request.session.get('uname')
    qs=Emails.objects.filter(user=uname)
    response=render(request,"allemails.html",context={'qs':qs})
    return response

def logout(request):
    request.session.flush()
    response=redirect(reverse_lazy("home"))
    return response



