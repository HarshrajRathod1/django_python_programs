from django.shortcuts import render
from formapp.forms import Person
# Create your views here.

def person_view(request):
    msg=""
    if request.method=="POST":
        form=Person(request.POST)
        if form.is_valid():
            msg="input data is valid"
        else:
            response=render(request,"person_temp.html",context={'form':form})
            return response
    
    form=Person()
    response=render(request,"person_temp.html",context={'form':form,'msg':msg})
    return response