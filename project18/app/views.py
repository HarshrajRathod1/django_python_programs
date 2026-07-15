from django.shortcuts import render
from app.forms import UserRegisterForm
from django.views import View 
from django.views.generic import TemplateView
from app.models import UserRegister
from django.http import HttpResponse
# Create your views here.
class RegisterView(View):
    def get(self,request):
        form=UserRegisterForm()
        response=render(request,"register.html",context={'form':form})
        return response
    def post(self,request):
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            msg="user created!"
            form=UserRegisterForm()
            response=render(request,"register.html",context={'msg':msg})
            return response 
        response=render(request,"register.html",context={'form':form})
        return response 
    
class Login_home(TemplateView):
    template_name="login.html"

class Login(View):
    def get(self,request):
        try:
            UserRegister.objects.get(uname=request.GET.get('uname'),password=request.GET.get('pwd'))
            output="<h2>Login</h2>"
            response=HttpResponse(output)
            return response
        except:
            msg="Inavalid Details"
            response=render(request,"login.html",context={'msg':msg})
            return response
        
class submit(TemplateView):
    template_name="submit.html"
    def get_context_data(self):
        context= super().get_context_data()
        context['name']="HARSH"
        context['age']=23
        return context



