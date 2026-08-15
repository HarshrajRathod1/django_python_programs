import requests 
import json

BASE_URL="http://127.0.0.1:8000/"

def getall():
    response=requests.get(BASE_URL+'getall/')
    print(response)
    print(response.json())

def getstud():
    rno=int(input("Enter Student Rollno : "))
    response=requests.get(BASE_URL+'getstud/'+str(rno)+"/")
    print(response)
    print(response.json())

def create_stud():
    rno=int(input("Enter Student Rollno : "))
    name=input('Enter Name : ')
    course=input('Enter Course : ')
    stud={'rno':rno,'name':name,'course':course}
    response=requests.post(BASE_URL+'create_stud/',data=stud)
    print(response)
    print(response.json())

def delete_stud():
    rno=int(input("Enter Student No : "))
    response=requests.delete(BASE_URL+"del_stud/"+str(rno)+"/")
    print(response)
    print(response.json())

def update_stud():
    rno=int(input("Enter Student No : "))
    course=input('Enter Course : ')
    response=requests.put(BASE_URL+"update_stud/"+str(rno)+"/"+str(course)+"/")
    print(response)
    print(response.json())

while True :
    print("="*50)
    print("\t 1. Get All Student Data")
    print("\t 2. Get Specific Student Data")
    print("\t 3. Create Student")
    print("\t 4. Update Student Data")
    print("\t 5. Delete Student Data")
    print("\t 6. Exit")
    print("="*50)

    ch=int(input("Enter Your Choice : "))

    match (ch):
        case 1:getall()

        case 2:getstud()

        case 3:create_stud()

        case 4:update_stud()

        case 5:delete_stud()

        case 6:break

        case _: print("Invalid Choice")
     

