import requests

endpoint = "http://localhost:8000/user/login/"


data = {
    "email": "test_email1@tes123.com",
    "password": "123..1213",
}
response = requests.post(endpoint, data)


# print(response.text)
print(response.status_code)
print(response.json())
