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

from django.core.serializers import serialize

def getallemp_view(request):
    qs=Employee.objects.all()
    data=serialize("json",qs)
    return JsonResponse(data,safe=False)    
import json
def getallemp_view1(request):
    qs=Employee.objects.all()
    json_data=serialize("json",qs,fields=['ename','job'])
    data=json.loads(json_data)
    fields_data=[]
    for obj in data:
        fields_data.append(obj['fields'])
    json_fields_data=json.dumps(fields_data)
    return JsonResponse(json_fields_data,safe=False)  

def insertemp_view(request):
    data=json.loads(request.body.decode('utf-8'))
    Employee.objects.create(ename=data['ename'],job=data['job'],sal=data['sal'])
    return JsonResponse({"msg":"Employee is created "},status=201)