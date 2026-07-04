from django.shortcuts import render

# Create your views here.
def view1(request):
    response=render(request,"temp1.html")
    return response 