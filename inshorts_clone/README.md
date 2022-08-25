# Relevel-Inshorts-clone

## Story 1: <b>Enable Purchases</b>

The task is to create an API endpoint “/ads/{adID}” to enable purchases:

The API request should take the input of the adID of the user along with the json object of the updated ad. In the interest of saving time, please use dummy adIDs.

There should be a key value pair of “Authorization: ” & if it's incorrect or not present API should throw Bad Request Exception with 401 Unauthorized code.

Apply proper validations for the value, for example, if the ad is not there, it should throw a 404 Not Found Exception.

Use an appropriate HTTPS method out of GET, POST, PUT, DELETE, etc. Display status & response code in the response.

The successful request should return 200 response code along with the purchase details

<br>

### Note from author.

Above instructions are a bit vague to me. Is it asking to create api for "seller to modify their ads and enable/disable sell of their goods" or "buyer to purchase goods with adID"?

`json of updated ad` -> points to former `purchase detail` -> points to later.

Part of both makes sense, not as a whole but in parts.
