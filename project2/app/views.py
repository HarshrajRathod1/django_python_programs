from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
student={'rollno':1,'name':'sugandh','course':'python'}
student_marks={'rollno':1,'sub1':50,'sub2':80}

def display_student(request):
    output=f'''<html>
    <body>
    <h2>Student data</h2>
    <table border="1" width=50%>
    <tr>
    <th>rollno</th>
    <th>name</th>
    <th>course</th>
    </tr>
    <tr>
    <td>{student['rollno']}</td>
    <td>{student['name']}</td>
    <td>{student['course']}</td>
    </tr>
    </table></body></html>'''
    response =HttpResponse(output)
    return response

def find_result(request):
    result="PASS" if student_marks['sub1']>=40 and student_marks['sub2']>=40 else "Fail"
    output=f'''<html>
    <body>
    <p>Rollno:{student_marks['rollno']}<br>
    Subject1:{student_marks["sub1"]}<br>
    subject2:{student_marks["sub2"]}<br>
    result:{result}</p></body></html>'''
    response=HttpResponse(output)
    return response

def home(request):
    dt=datetime.datetime.today()
    t=dt.time()
    h=t.hour
    if h>=5 and h<12:
        msg="Good Morning"
    elif h>=12 and h<17:
        msg="Good Afternoon"
    else:
        msg="Good Evening"
    output=f'''<html>
    <body>
    <h2>{msg},Welcome to My Page</h2></body></html>'''
    response=HttpResponse(output)
    return response 

