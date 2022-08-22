import requests


bookingID = "5woaUX"

endpoint = f"http://localhost:8000/booking/detail/{bookingID}/"

response = requests.get(endpoint)


# print(response.text)
print(response.status_code)
print(response.json())
