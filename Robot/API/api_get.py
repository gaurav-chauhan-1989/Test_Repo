
from API.API_methods import api_method

api_met = api_method()

url = 'https://reqres.in/api/users/534'

response = api_met.api_get_method(url)
print(response)
if response[0]['first_name'] == 'Janet':
    print(True)
else:
    print(False)
