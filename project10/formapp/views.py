from django.shortcuts import render
from formapp.forms import Register
from formapp.models import UserRegister
# Create your views here.

def register(request):
    if request.method=="POST":
        form=Register(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            uname = form.cleaned_data['uname']
            password = form.cleaned_data['password']

            UserRegister.objects.create(name=name,uname=uname,password=password)

            response=render(request,"register_temp.html",context={'msg':"data saved!"})
            return response 



    form=Register()
    response=render(request,"register_temp.html",context={'form':form})
    return response
