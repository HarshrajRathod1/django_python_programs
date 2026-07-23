from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    response=render(request,"home.html")
    return response

def calc(request):
    request.session["n1"]=request.GET.get('t1')
    request.session["n2"]=request.GET.get('t2')
    response=render(request,"calc_temp.html")
    return response

def calculate(request):
    num1=int(request.session.get('n1'))
    num2=int(request.session.get('n2'))
    if (request.GET.get('add')):
        num3=num1+num2
    else:
        num3=num1-num2
    response=HttpResponse(f"<h2>Result is ={num3}</h2>")
    return response
