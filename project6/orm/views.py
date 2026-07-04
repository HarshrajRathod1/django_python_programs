from django.shortcuts import render
from orm.models import Books,Marks
# Create your views here.
def home(request):
    response=render(request,"home.html")
    return response 

def insert_book(request):
    id=request.POST.get("bid")
    name=request.POST.get("bname")
    b=Books(bookid=id,bname=name)
    b.save()
    response=render(request,"home.html",context={'msg':"saved"})
    return response 

def homeFind(request):
    response=render(request,"insert.html")
    return response 

def showresult(request):
    rno=request.GET.get("rno")
    try:
        student=Marks.objects.get(rolno=rno)
        total=student.sub1+student.sub2
        avg=total/2
        result="PASS" if student.sub1>=40 and student.sub2>=40 else "Fail"
        stud={
            'rno':student.rolno,
            'sub1':student.sub1,
            'sub2':student.sub2,
            'total':total,
            'avg':avg,
            'result':result
        }
        response=render(request,"stud_marks.html",context={'stud':stud})
    except:
        response=render(request,"insert.html",context={'msg':'Invalid Roll Number'})
    return response

def findresultall(request):
    qs=Marks.objects.all()
    studs=[]
    for stud in qs:
        s={'rno':stud.rolno,
           'sub1':stud.sub1,
           'sub2':stud.sub2,
           'total':stud.sub1+stud.sub2,
           'avg':(stud.sub1+stud.sub2)/2,
           'result':"PASS" if stud.sub1>=40 and stud.sub2>=40 else "FAIL"}
        studs.append(s)
    response=render(request,"results_all.html",context={'stud':studs})
    return response 
from orm.models import Employee
def findjob(request):
    job=request.GET.get("job")
    qs=Employee.objects.filter(job=job)
    response=render(request,"find_job.html",context={'qs':qs})
    return response 
def findjobhome(request):
    response=render(request,"find_job.html")
    return response