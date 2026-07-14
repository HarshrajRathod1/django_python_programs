from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.http import HttpResponse
# Create your views here.

class First_View(View):
    def get(self,request):
        output="<h2>This is get request</h2>"
        response=HttpResponse(output)
        return response
    
    def post(self,request):
        output="<h2>This is a post request</h2>"
        response=HttpResponse(output)
        return response
    
class display(TemplateView):
    template_name="first_temp.html"
