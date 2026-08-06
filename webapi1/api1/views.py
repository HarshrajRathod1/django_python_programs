from django.shortcuts import render
from django.http import HttpResponse
from json import dumps
# Create your views here.

def view1(request):
    stud={'rolno':1,'name':'rahul','course':'python'}
    output=f'''<html><body>
    <p>Student RollNo : {stud['rolno']}<br>
    Student Name : {stud['name']}<br>
    Student Course : {stud['course']}</p>
    </body></html>'''
    return HttpResponse(output)

def view2(request):
    stud={'rolno':1,'name':'rahul','course':'python'}
    stud_json=dumps(stud)
    return HttpResponse(stud_json,content_type="application/json")

from django.http import JsonResponse

def view3(request):
    stud={'rolno':1,'name':'rahul','course':'python'}
    return JsonResponse(stud)
