import requests
import json
BASE_URL="http://localhost:8000/"
END_POINT="getallemp/"

response=requests.get(BASE_URL+END_POINT)
print(response)
print(response.json())
data=response.json()
print(type(data))
print('-'*50)
END_POINT="getallemp1/"
response=requests.get(BASE_URL+END_POINT)
print(response)
print(response.json())
data=response.json()
print(type(data))
print('-'*50)
END_POINT="insertemp/"
emp={
    "ename":input("Enter Employee Name : "),
    "job":input("Enter job Role : "),
    "sal":float(input("Enter Your salary : "))
}
json_data=json.dumps(emp)
response=requests.post(BASE_URL+END_POINT,data=json_data)
print(response)
print(response.text)
