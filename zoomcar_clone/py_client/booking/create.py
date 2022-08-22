import requests

endpoint = "http://localhost:8000/booking/create/"

Token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYxMTc2MzE1LCJpYXQiOjE2NjExNzU3MTUsImp0aSI6IjgxNTUwZWQzOTQ1MDRkNzViMmUzMGU0ZmI4N2Y4OTk2IiwidXNlcl9pZCI6Nn0.mjxXEtlH17ZZcqlJwqF7R89_Nzk8c-OTz_k8lYEWoso"

data = {
    "vehicle": "maruti",
    "starting_date": "2022-12-24",
    "duration": "4",
}

response = requests.post(endpoint, data, headers={'Authorization': f'Bearer {Token}'})


# print(response.text)
print(response.status_code)
print(response.json())
