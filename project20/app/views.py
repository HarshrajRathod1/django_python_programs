from django.shortcuts import render
from django.views.generic import DetailView
from app.models import Employee


# Create your views here.

class EmpDetailView(DetailView):
    model=Employee
    context_object_name="emp"

class EmpDetailView1(DetailView):
    model=Employee
    context_object_name="emp"

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        e=super().get_object()
        comm=e.sal*10/100
        context["comm"]=comm
        print(context)
        return context
    
from django.views.generic import UpdateView,ListView
from app.forms import EmployeeForm
class EmpUpdateView(UpdateView):
    model=Employee
    form_class=EmployeeForm
    success_url="/emp_list"

class EmpList(ListView):
    model=Employee
    context_object_name="emp"


        
    

