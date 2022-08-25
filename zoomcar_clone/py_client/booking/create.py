import requests

endpoint = "http://localhost:8000/booking/create/"

Token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYxNDM3NzAzLCJpYXQiOjE2NjE0MzcxMDMsImp0aSI6ImMxYjIyYTA2MWRmNDRhOTY4NDZkNDhkNWFjNmNhNjQ3IiwidXNlcl9pZCI6OX0.n2iX-Q9gNVIiF_Pn8i3WlqTdF9X9akCpPn3K_TV77Is"

data = {
    "vehicle": "maruti",
    "starting_date": "2022-12-24",
    "duration": "4",
}

response = requests.post(endpoint, data, headers={'Authorization': f'Bearer {Token}'})


# print(response.text)
print(response.status_code)
print(response.json())
