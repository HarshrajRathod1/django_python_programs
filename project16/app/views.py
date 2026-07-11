from django.shortcuts import render
from .forms import StudentForm
from .models import Student
# Create your views here.

def add_student(request):
    msg=""
    if request.method=="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            msg="Form Data Saved"
        else:
            response=render(request,"add_stud_temp.html",context={'form':form})
            return response 
        
    form=StudentForm()
    response=render(request,"add_stud_temp.html",context={'form':form,'msg':msg})
    return response

def find_result_home(request):
    response=render(request,"find_result.html")
    return response

def find_result(request):
    rolno=request.GET.get("rolno")
    try:
        stud=Student.objects.get(rollno=rolno)
        result=stud.find_result()
        total=stud.get_total()
        avg=stud.get_avg()
        response=render(request,"find_result.html",context={'stud':stud,'total':total,'avg':avg,'result':result})
        return response
    except:
        response=render(request,"find_result.html",context={'msg':"Invalid roll no"})
        return response


