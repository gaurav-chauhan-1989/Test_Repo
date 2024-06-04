from API.API_methods import api_method

coreapi = api_method()

url = 'https://reqres.in/api/users/534'
payload_file = "E:\\user_update.json"

response = coreapi.api_patch_method(url, payload_file)
print(response)