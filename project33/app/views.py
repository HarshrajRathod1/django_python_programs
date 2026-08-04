from django.shortcuts import render
from app.models import Employess
# Create your views here.

def home_view(request):
    return render(request,"emp_details_temp.html")

def emp_range_emp(request):
    min=request.GET.get('min')
    max=request.GET.get('max')
    qs=Employess.objects.filter(sal__gte=min,sal__lte=max)
    return render(request,"emp_details_temp.html",context={'qs':qs})

def filter_job_view(request):
    val=request.GET.get('job')
    qs=Employess.objects.filter(job=val)
    return render(request,"emp_details_temp.html",context={'qs':qs})

