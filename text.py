import requests
#response=requests.get("http://127.0.0.1:8000/v1/")
#response=requests.get("http://127.0.0.1:8000/v2/")
response=requests.get("http://127.0.0.1:8000/v3/")
print(response)
print(type(response))
print(response.text)
print(type(response.text))
print('-'*50)