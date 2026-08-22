import requests
import json 

BASE_URL="http://127.0.0.1:8000/"

def emp_list():
    response=requests.get(BASE_URL+"emplist/")
    print(response.json())

def emp_get():
    eno=int(input("Enter Employee No : "))
    response=requests.get(BASE_URL+"empget/"+str(eno)+"/")
    print(response.json())

def emp_create():
    emp_dict={
        'eno':int(input("Enter Employee No : ")),
        'ename':input("Enter Employee Name : "),
        'job':input("Enter Employee Job : "),
        'salary':float(input("Enter Employee Salary : "))
    }
    headers={'Content-Type':'application/json'}
    response=requests.post(BASE_URL+"empcreate/",json=emp_dict,headers=headers)
    print(response.json())

def emp_update_all():
    eno=int(input("Enter Employee No : "))
    ename=input("Enter Employee Name : ")
    job=input("Enter Employee Job : ")
    salary=float(input("Enter Employee Salary : "))
    emp_dict={
        'eno':eno,
        'ename':ename,
        'job':job,
        'salary':salary
    }
    headers={'Content-Type':'application/json'}
    response=requests.put(BASE_URL+"empupdate/"+str(eno)+"/",json=emp_dict,headers=headers)
    print(response.json())

def emp_update_name():
    eno=int(input("Enter Employee No : "))
    ename=input("Enter Employee Name : ")
    emp_dict={
        'eno':eno,
        'ename':ename,
    }
    headers={'Content-Type':'application/json'}
    response=requests.patch(BASE_URL+"empupdate/"+str(eno)+"/",json=emp_dict,headers=headers)
    print(response.json())


def emp_delete():
    eno=int(input("Enter Employee No : "))
    response=requests.delete(BASE_URL+"empdelete/"+str(eno)+"/")
    if(response.status_code==204):
        print('Employee Delete')
    else:
        print(response.status_code)


#emp_create()
#emp_list()
#emp_get()
#emp_update_all()
emp_update_name()
#emp_delete()