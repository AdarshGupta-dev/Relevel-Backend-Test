import requests

endpoint = "http://localhost:8000/booking/create/"

Token = ""

data = {
    "vehicle": "maruti",
    "starting_date": "2022-12-24",
    "duration": "4",
    "renter": "1",
}

response = requests.post(endpoint, data, headers={'Authorization': f'Bearer {Token}'})


# print(response.text)
print(response.status_code)
print(response.json())
