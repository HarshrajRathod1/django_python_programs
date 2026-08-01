from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def view1(request):
    return HttpResponse("<h1>View 1</h1>")

def view2(request):
    return render(request,"temp1.html",context={'client_data':request.headers})


