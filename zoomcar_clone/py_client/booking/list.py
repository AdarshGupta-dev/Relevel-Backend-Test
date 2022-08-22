import requests

endpoint = "http://localhost:8000/booking/list/"

Token = ""

response = requests.get(endpoint, headers={'Authorization': f'Bearer {Token}'})


# print(response.text)
print(response.status_code)
print(response.json())
