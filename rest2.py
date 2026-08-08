import requests
import json
BASE_URL="http://localhost:8000/"
END_POINT="allemployess"

response=requests.get(BASE_URL+END_POINT)
print(response)
print(response.json(),type(response.json()))#List
print("-"*50)
for emp in response.json():
    print(emp)
print("-"*50)

END_POINT="get_emp/"
empno=input("Enter Employee Number :")
print(BASE_URL+END_POINT+empno+"/")
response=requests.get(BASE_URL+END_POINT+empno)

print(response)
print(response.json(),type(response.json())) #dict