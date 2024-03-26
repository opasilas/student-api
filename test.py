# from email import header
import requests, json

BASE_URL = "http://127.0.0.1:8000/api/v1/students"
data = {'name': 'Opa', 'email': 'opa8@gmail.com'}
headers = {'Content-Type': 'application/json'}


response = requests.get(BASE_URL)
print(response.json())

input()

# response = requests.post(BASE_URL, data=json.dumps(data), headers=headers)
# print(response.json())

# input()

# delete = requests.delete(BASE_URL + '/9')
# print(delete.json())

health = requests.get(BASE_URL + '/health')
print(health.json())
# clear = requests.delete(BASE_URL)
# print(clear.json())