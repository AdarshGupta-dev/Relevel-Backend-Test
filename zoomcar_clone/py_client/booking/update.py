import requests

bookingID = "5woaUX"

Token = ""
data = {
    "vehicle": "maruti",
    "starting_date": "2022-12-24",
    "duration": "4",
}

endpoint = f"http://localhost:8000/booking/update/{bookingID}/"

response = requests.patch(endpoint, data, headers={'Authorization': f'Bearer {Token}'})

# print(response.text)
print(response.status_code)
print(response.json())
