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

from django.db.models import Max,Min,Avg,Count,Sum

def group_by(request):
    job=request.GET.get('job')
    func=request.GET.get('function')
    if job=="all":
          match func:
                  case 'max':
                          qs=Employess.objects.values('job').annotate(res=Max('sal'))
                  case 'min':
                          qs=Employess.objects.values('job').annotate(res=Min('sal'))
                  case 'avg':
                          qs=Employess.objects.values('job').annotate(res=Avg('sal'))
                  case 'count':
                          qs=Employess.objects.values('job').annotate(res=Count('sal'))
                  case 'sum':
                          qs=Employess.objects.values('job').annotate(res=Sum('sal'))
    else:
        match func:
            case 'max':
                    qs=Employess.objects.values('job').annotate(res=Max('sal')).filter(job=job)
            case 'min':
                    qs=Employess.objects.values('job').annotate(res=Min('sal')).filter(job=job)
            case 'avg':
                    qs=Employess.objects.values('job').annotate(res=Avg('sal')).filter(job=job)
            case 'count':
                    qs=Employess.objects.values('job').annotate(res=Count('sal')).filter(job=job)
            case 'sum':
                    qs=Employess.objects.values('job').annotate(res=Sum('sal')).filter(job=job)
    return render(request,"agg_temp.html",context={'qs':qs})

def agg_home_view(request):
    return render(request,"agg_temp.html")

