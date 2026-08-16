import requests
import json

BASE_URL="http://127.0.0.1:8000/"
def empno():
    empno=int(input("Enter Employee No : "))
    return empno

def empdata():
    name=input('Enter Employee Name : ')
    job=input('Enter Employee Job : ')
    salary=float(input('Enter Salary : '))
    emp={'ename':name,'job':job,'sal':salary}
    return emp

def getall_emp():
    response=requests.get(BASE_URL+"emp/")
    print(response)
    print(response.json())

def get_emp():
    eno=empno()
    response=requests.get(BASE_URL+"emp/"+str(eno)+"/")
    print(response)
    print(response.json())

def create_emp():
    eno=empno()
    empdict=empdata()
    empdict['eno']=eno
    response=requests.post(BASE_URL+'emp/',data=empdict)
    print(response)
    print(response.json())

def update_emp():
    eno=empno()
    emp_dict=empdata()
    emp_dict['eno']=eno
    response=requests.put(BASE_URL+'emp/'+str(eno)+"/",data=emp_dict)
    print(response)
    print(response.json())

def delete_emp():
    eno=empno()
    response=requests.delete(BASE_URL+'emp/'+str(eno)+'/')
    print(response)
    print(response.json())

while True :
    print("="*50)
    print("\t1. Get all Employee")
    print("\t2. Get Employee")
    print("\t3. Create Employee")
    print("\t4. Update Employee")
    print("\t5. Delete Employee")
    print("\t6. Exit")
    print("="*50)
    try:
        ch=int(input("What you Want Enter : "))
    except:
        print("Enter Only Number")

    match (ch):
        case 1:
            getall_emp()
        case 2:
            get_emp()
        case 3:
            create_emp()
        case 4:
            update_emp()
        case 5:
            delete_emp()
        case 6:
            break
        case _:
            print("Please Select Valid Choice")

