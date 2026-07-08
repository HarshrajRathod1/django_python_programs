from django.shortcuts import render
from app.forms import RegisterForm
# Create your views here.
def register_view(request):
    msg=""
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid:
            form.save()
            msg="employee data saved"
        else:
            response=render(request,"emp_temp.html",context={'form':form})
            return response
    form=RegisterForm()
    response=render(request,"emp_temp.html",context={'form':form,'msg':msg})
    return response
