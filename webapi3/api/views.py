from django.shortcuts import render
from api.models import Employee
from django.http import JsonResponse
import json
# Create your views here.

def allemployess(request):
    qs=Employee.objects.all()
    emp_list=[]
    for emp in qs:
        data={'empno':emp.empno,'ename':emp.ename,'sal':emp.sal,'job':emp.job}
        emp_list.append(json.dumps(data))
    return JsonResponse(emp_list,safe=False)

def single_emp(request,empno):
    try:
        emp=Employee.objects.get(empno=int(empno))
        emp_data={'empno':emp.empno,'ename':emp.ename,'job':emp.job,'sal':emp.sal}
        return JsonResponse(emp_data)
    except:
        return JsonResponse({"msg":"Invalid Employee Number"})


        


