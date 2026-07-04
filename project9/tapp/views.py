from django.shortcuts import render

# Create your views here.
def view1(request):
    response=render(request,"child.html")
    return response 
def view2(request):
    response=render(request,"temp1.html")
    return response

from tapp.forms import loginForm

def login(request):
    fo=loginForm()
    response=render(request,"login_page.html",context={'fo':fo})
    return response 
