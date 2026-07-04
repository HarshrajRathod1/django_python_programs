from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    response=render(request,"home.html")
    return response

def register(request):
    name=request.POST.get("name")
    uname=request.POST.get("uname")
    pwd=request.POST.get("pwd")
    print(name)
    print(uname)
    print(pwd)
    output="""<html>
    <body>
    <h2>Hi,{{name}} Welcome💕</h2>
    <p>Your username is {uname}</p>
    <p>Your Password is {pwd}</p>
    </body></html>"""
    response=HttpResponse(output)
    return response