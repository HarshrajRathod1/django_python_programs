from django.shortcuts import render

# Create your views here.

def login(request):
    users={
        "rahul":"r123",
        "kamlesh":"k123",
        "mahesh":"m123"
    }
    uname=request.GET.get("uname")
    pwd=request.GET.get("pwd")
    if uname in users and users[uname]==pwd:
        response=render(request,"index.html",context={"uname":uname})
        return response 
    else:
        response=render(request,"login.html",context={"msg":"Invalid Details Try again"})
        return response
    
def home(request):
    response=render(request,"login.html")
    return response