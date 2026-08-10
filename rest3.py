import requests
import json 

BASE_URL="http://127.0.0.1:8000/"
while True:
    print("*"*50)
    print("\t1. List All Employess")
    print("\t2. Get Employee")
    print("\t3. Create Employee")
    print("\t4. Update Employee")
    print("\t5. Delete Employee")
    print("\t6. Exit\n")
    print("="*50)
    

    ch=int(input("Enter Your Choice : "))
    match ch:
        case 1:
            END_POINT="getallemp1/"
            response=requests.get(BASE_URL+END_POINT)
            data=response.json()
            print("\t",data)
        case 2:
            empno=int(input("Enter Employee No. : "))
            END_POINT="get_emp/"+str(empno)+"/"
            response=requests.get(BASE_URL+END_POINT)
            data=response.json()
            print("\t",data)
        case 3:
            emp_dict={
                'empno':int(input("Enter Employee No. : ")),
                'ename':input("Enter Employee Name : "),
                'job':input("Enter Employee Job Designation : "),
                'sal':float(input("Enter Employee Salary : "))
            }
            emp_json=json.dumps(emp_dict)
            END_POINT="insertemp/"
            response=requests.post(BASE_URL+END_POINT,data=emp_json)
            data=response.json()
            print("\t",data)
        case 4:
            emp_dict={"empno":input('Enter Your Employee Number : '),"sal":input("Enter Your Salary : ")}
            emp_json=json.dumps(emp_dict)
            END_POINT="updateemp/"
            response=requests.put(BASE_URL+END_POINT,data=emp_json)
            data=response.json()
            print("\t",data)
        case 5:
            #http://127.0.0.1:8000/delemp/8
            empno=int(input("Enter Your Employee No. : "))
            END_POINT="delemp/"+str(empno)+"/"
            response=requests.delete(BASE_URL+END_POINT)
            data=response.json()
            code=response.status_code
            print(code)
            if code==200:
                print("\t",data['msg'])
            else:
                print("\t",data['msg'])
            #print("URL:", BASE_URL + END_POINT)
            #print("Status:", response.status_code)
        case 6:
            print("\t\t Thanx for using")
            break 
        case _: print("You Selected Wrong Choice!")
        
