import requests
import json

BASE_URL="http://127.0.0.1:8000/"

def getall_emp():
    response=requests.get(BASE_URL+'getall/')
    print(response)
    print(response.json())

def getemp():
    eno=int(input("Enter Employee No : "))
    response=requests.get(BASE_URL+'getemp/'+str(eno)+'/')
    print(response)
    print(response.json())

def create_emp():
    eno=int(input("Enter Employee No : "))
    ename=input('Enter Employee Name : ')
    sal=float(input('Enter salary : '))
    job=input('Enter Job : ')
    emp={'eno':eno,'ename':ename,'job':job,'sal':sal}
    emp_json=json.dumps(emp)
    response=requests.post(BASE_URL+'empcreate/',data=emp_json)
    print(response)
    print(response.json())

getall_emp()
getemp()
#create_emp()