import requests
import json
import jsonpath
import pickle
from API.API_methods import api_method

coreapi = api_method()
url = 'https://reqres.in/api/users'
json_file = "E:\\user_create.json"

response = coreapi.api_post_method(url, json_file)
print(response)
fileobj = open("usr.json", "wb")                                   # Creating file to store data in write byte format
pickle.dump(response, fileobj)                                     # Dump data using pickle
if response['name'] == 'Gaurav':
    print(True)
else:
    print(False)
'''fileobj1 = open("usr.json", "rb")                               # Open file in read byte mode     
s = pickle.load(fileobj1)                                          # Load data using pickle
print(s)'''

#content = f.read()
'''json_content = json.loads(content)
response = requests.post(url, json_content)
json_response = json.loads(response.text)
job_data = jsonpath.jsonpath(json_response, 'job')
print(job_data[0])
assert response.status_code == 201'''

