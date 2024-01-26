- This function takes a password reset token as input and returns the email associated with it if the token is valid, otherwise returns `None`.
- It uses Django's built-in JWT library to decode the token and extract its payload (which includes an "email" field).
- The secret key used for signing/verifying tokens is retrieved from the project's settings file using the `settings` object provided by Django itself.