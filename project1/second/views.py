from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def second(request):
    output='''<html>
    <body bgcolor=pink>
    <h2>Welcome to second page</h2>
    </body>
    </html>'''
    response=HttpResponse(output)
    return response 

def third(request):
    output='''<html>
    <body bgcolor=red>
    <h2>Welcome to second page</h2>
    </body>
    </html>'''
    response=HttpResponse(output)
    return response
