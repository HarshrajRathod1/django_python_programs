from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import RedirectView
# Create your views here.

def view1(request):
    msg="<h2>This is view1</h2>"
    response=HttpResponse(msg)
    return response

def view2(request):
    response=redirect(view1)
    return response

class view3(RedirectView):
    url="http://www.youtube.com"

class view4(RedirectView):
    url="/view1"