# Relevel-Zoomcar-Clone

## Story 1. User Model

The task is to create a User and Booking model to store key information of all the users.

The various functionalities to develop under this story are:

a. User model should be able to store Name, Email/Phone, Password, Gender, Date of Birth.

b. Booking model should hold all references to bookings and should be mapped to users using their IDs.

c. Appropriate constraints including primary key should be there.

d. Create migrations & migrate it to make the changes at Database level.

<br>

## Story 2. Login API

The task is to create an API endpoint “/login” for the login/authentication of the user:

a. The API request should take the input of Email/Phone & Password.

b. Authenticate the values and generate a JWT token..

c. Use an appropriate HTTPS method out of GET, POST, PUT, DELETE, etc.

d. In case of incorrect credentials API response should throw 401 Unauthorized Exception.

e. The successful request should return 201 response code along with the JWT token which will be used for authorization in subsequent requests.
