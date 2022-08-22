import requests


bookingID = "5woaUX"
Token = ""

endpoint = f"http://localhost:8000/booking/detail/{bookingID}/"

response = requests.get(endpoint, headers={'Authorization': f'Bearer {Token}'})


# print(response.text)
print(response.status_code)
print(response.json())
