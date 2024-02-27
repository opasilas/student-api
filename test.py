from email import header
import requests, json

BASE_URL = "http://127.0.0.1:5000/api/v1/students"
data = {'name': 'Silas', 'email': 'opasilas1@gmail.com'}
headers = {'Content-Type': 'application/json'}


response = requests.get(BASE_URL)
print(response.json())

input()

response = requests.post(BASE_URL, data=json.dumps(data), headers=headers)
print(response.json())

delete = requests.delete(BASE_URL + '/2')
print(delete.json())