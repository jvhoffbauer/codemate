- Generates a password reset token for a given email address using Django's built-in `django.contrib.auth.hashers` module and JWT (JSON Web Token).
- The token is valid for a specified number of hours as defined in the `settings.py` file.
- The function returns the generated token as a string.