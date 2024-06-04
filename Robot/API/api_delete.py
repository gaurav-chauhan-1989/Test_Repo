from API.API_methods import api_method

coreapi = api_method()

url = 'https://reqres.in/api/users/75'

response = coreapi.api_delete_method(url)
print(response)
