- Endpoint to obtain a new access token using a refresh token
- Uses `jwt.decode()` to verify the refresh token and extract the necessary data from it
- Checks that the decoded payload contains a valid refresh token and has not expired
- Retrieves the associated user record from the database based on the subject of the decoded payload
- Returns a new access token with the ID of the retrieved user as its subject