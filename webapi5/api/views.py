from django.shortcuts import render
from api.models import Employee
from api.serializers import EmployeeSerializers
from rest_framework.views import Response
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
import io
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
# Create your views here.

def getall_emp(request):
    qs=Employee.objects.all()
    empseri=EmployeeSerializers(qs,many=True)
    emp_list=empseri.data
    emp_json=JSONRenderer().render(emp_list)
    print(type(emp_json))
    return HttpResponse(emp_json,content_type="application/json")

def getemp(request,eno):
    emp=Employee.objects.get(eno=eno)
    empser=EmployeeSerializers(emp)
    emp_data=empser.data
    emp_json=JSONRenderer().render(emp_data)
    return HttpResponse(emp_json,content_type="application/json")

@csrf_exempt
def createemp(request):
    stream=request.body
    print("stream type=",type(stream),"-> data stream =",stream)
    bytes=io.BytesIO(stream)
    print("bytes type =",type(bytes),"-> data bytes =",bytes)
    dict_data=JSONParser().parse(bytes)
    print("dict_data type =",type(dict_data),"-> data dict_data =",dict_data)
    emp_ser=EmployeeSerializers(dict_data)
    print("emp_ser type =",type(emp_ser),"-> data emp_ser =",emp_ser)
    emp_dict=emp_ser.data
    print("emp_dict type =",type(emp_dict),"-> data emp_dict =",emp_dict)
    emp=Employee.objects.create(eno=emp_dict["eno"],ename=emp_dict['ename'],sal=emp_dict['sal'],job=emp_dict['job'])
    emp.save()
    return HttpResponse(json.dumps({'msg':'Employee Created'}),content_type="application/json")


