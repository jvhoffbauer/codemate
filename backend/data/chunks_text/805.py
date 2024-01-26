- Generates a JSON Web Token (JWT) with a payload containing the user's ID and admin status
- Expires after a specified time interval defined by `expires_delta`
- Uses Flask-JWT-Extended to encode the JWT using a secret key and HMAC SHA256 encryption algorithm