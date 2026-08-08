import requests

BASE_URL="http://127.0.0.1:8000/"
END_POINT="v1/"
print("Function Based View")
response=requests.get(BASE_URL+END_POINT)
print(response.json(),type(response.json()))#Dict
print(response.text,type(response.text))#STR
print("-"*50)
response=requests.post(BASE_URL+END_POINT)
print(response.json(),type(response.json()))#Dict
print(response.text,type(response.text))#STR
print("-"*50)
response=requests.put(BASE_URL+END_POINT)
print(response.json(),type(response.json()))#Dict
print(response.text,type(response.text))#STR
print("-"*50)
response=requests.delete(BASE_URL+END_POINT)
print(response.json(),type(response.json()))#Dict
print(response.text,type(response.text))#STR
print("-"*50)

print("Class Based View")
END_POINT="hdfc/"
response=requests.get(BASE_URL+END_POINT)
print(response.json(),type(response.json())) #DICT
print(response.text,type(response.text)) #STR
print("-"*50)
response=requests.post(BASE_URL+END_POINT)
print(response.json(),type(response.json())) #DICT
print(response.text,type(response.text)) #STR
print("-"*50)
response=requests.put(BASE_URL+END_POINT)
print(response.json(),type(response.json())) #DICT
print(response.text,type(response.text)) #STR
print("-"*50)
response=requests.delete(BASE_URL+END_POINT)
print(response.json(),type(response.json())) #DICT
print(response.text,type(response.text)) #STR
print("-"*50)