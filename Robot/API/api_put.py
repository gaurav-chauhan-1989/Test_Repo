import requests
import json
import jsonpath

url = 'https://reqres.in/api/users/2'
f = open("E:\\user_update.json", 'r')

content = f.read()
json_content = json.loads(content)
response = requests.put(url, json_content)
json_response = json.loads(response.text)
job_data = jsonpath.jsonpath(json_response, 'job')
print(job_data[0])
assert response.status_code == 200