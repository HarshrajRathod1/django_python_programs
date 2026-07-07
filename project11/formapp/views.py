from django.shortcuts import render
from formapp.forms import RegisterForm
from formapp.models import UserRegister
# Create your views here.

def register_view(request):
    msg=""
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            name=request.POST.get("name")
            uname=request.POST.get("uname")
            password=request.POST.get("password")
            UserRegister.objects.create(name=name,uname=uname,password=password)
            msg="User Created"
        else:
            response=render(request,"register_temp.html",context={'form':form})
            return response

    form=RegisterForm()
    response=render(request,"register_temp.html",context={'form':form,'msg':msg})
    return response
