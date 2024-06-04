import json

json_string = '{ "id": 121, "name": "Naveen", "course": "MERN Stack"}'

dic_string = json.loads(json_string)
key_list = list(dic_string.keys())
value_list = list(dic_string.values())

print(key_list)
print(value_list)

print(type(key_list))