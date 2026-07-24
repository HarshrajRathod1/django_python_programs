from django.shortcuts import render
from app.models import Users,Emails
# Create your views here.

def login_home(request):
    response=render(request,"login_temp.html")
    return response

def login(request):
    uname=request.GET.get("uname")
    pwd=request.GET.get("pwd")
    try:
        if (Users.objects.get(uname=uname,password=pwd)):
            request.session['uname']=uname
            request.session['pwd']=pwd
            response=render(request,"inbox_temp.html")
            return response
    except:
        response=render(request,"login_temp.html",context={'msg':"Invalid UserName Password"})
        return response


def viewmails(request):
    qs=Emails.objects.filter(uname=request.session.get('uname'))
    print(qs[0].uname)
    response=render(request,"mails_temp.html",context={'qs':qs})
    return response

def logout(request):
    session=list(request.session.items())
    print(session)
    if session[0][0]==0:
        response=render(request,"login_temp.html")
        return response
    else:
        request.session.pop('uname')
        response=render(request,"login_temp.html")
        return response
    