from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def first(request):
    output="""<html>
    <body bgcolor=cyan>
        <h1>Hello World</h1>
    </body>
    </html>"""
    response=HttpResponse(output)
    return response


def view1(request):
    return HttpResponse("<h1>View 1 </h1>")

def view2(request):
    return HttpResponse("<h1>View 2 </h1>")