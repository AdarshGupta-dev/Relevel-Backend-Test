import requests

endpoint = "http://localhost:8000/user/register/"


data = {
    "email": "test2email1@tes123.com",
    "name": "test name",
    "password": "123..123",
    "gender": "M",
    "date_of_birth": "1999-12-12",
}
response = requests.post(
    endpoint,
    data
)


# print(response.text)
print(response.status_code)
print(response.json())
