import requests
import json

BASE_URL="http://127.0.0.1:8000/"

def insert_student():
    stud={
        "rollno":int(input("Enter Rollno : ")),
        "name":input("Enter Name : "),
        "course":input("Enter Course : "),
        "fee":float(input("Enter Fees : "))
    }
    stud_json=json.dumps(stud)
    print(stud_json)
    END_POINT="stud/"
    print(BASE_URL+END_POINT)
    response=requests.post(BASE_URL+END_POINT,data=stud_json)
    print(response)

def get_student():
    rollno=int(input("Enter Rollno : "))
    END_POINT="stud/"+str(rollno)+"/"
    response=requests.get(BASE_URL+END_POINT)
    print(response)
    print(response.json())

def delete_student():
    rollno=int(input("Enter Rollno : "))
    END_POINT="stud/"+str(rollno)+"/"
    response=requests.delete(BASE_URL+END_POINT)
    print(response)

def update_student():
    data={"rollno":int(input("Enter Rollno : ")),
          "fee":float(input("Enter Fees : "))}
    data_json=json.dumps(data)
    END_POINT="stud/"
    response=requests.put(BASE_URL+END_POINT,data=data_json)
    print(response)
    print(response.json())

insert_student()
#get_student()
#update_student()
#delete_student()


