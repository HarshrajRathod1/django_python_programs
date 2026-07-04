from django.shortcuts import render

# Create your views here.
def home(request):
    response=render(request,'First.html') 
    return response
def addnum(request):
    a=100
    b=200
    c=a+b
    response=render(request,"result.html",context={"a":a,"b":b,"c":c})
    return response 

def findresult(request,rno):
    marks={1:['naresh',70,70],
           2:['ramesh',80,50],
           3:['suresh',40,30]}
    if rno in marks:
        stud=marks[rno]
        result="Pass" if stud[1]>=40 and stud[2]>=40 else "Fail"
        response=render(request,"studresult.html",context={'rno':rno,'stud':stud,'result':result})
        return response 
    else:
        response=render(request,"error.html",msg="invalid rollno")
        return response

def calc(request,a,b,opr):
    match(opr):
        case "+": 
            c=a + b
        case "-": 
            c=a-b
        case "*":
            c=a*b
        case "/":
            c=a/b
        case _:
            c=None
    response=render(request,"calctemp.html",context={"a":a,"b":b,"c":c,"opr":opr})
    return response

def finalresult1(request):
    marks={1:['naresh',70,70],
           2:['ramesh',80,50],
           3:['suresh',40,30]}
    rno=int(request.GET.get("rno"))
    if rno in marks:
        stud=marks[rno]
        result="Pass" if stud[1]>=40 and stud[2]>=40 else "Fail"
        response=render(request,"studresult.html",context={'rno':rno,'stud':stud,'result':result})
        return response 
    else:
        response=render(request,"error.html",msg="invalid rollno")
        return response
    
            