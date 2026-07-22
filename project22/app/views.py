from django.shortcuts import render
from app.models import Student
from app.forms import StudentForm
from django.views import View 
from django.views.generic import ListView
# Create your views here.

class CreateStudentView(View):
    def get(self,request):
        form=StudentForm()
        response=render(request,"stud_temp.html",context={'form':form})
        return response
    def post(self,request):
        msg=''
        form=StudentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            msg="form is save"
            response=render(request,"stud_temp.html",context={'form':form,'msg':msg})
        else:
            response=render(request,"stud_temp.html",context={'form':form,})
        return response

class StudentListView(ListView):
    model=Student
    context_object_name="student"
    template_name="stud_all_lists_temp.html"
