- Takes in a plain text password and a salted and hashed password as arguments
- Uses Python's built-in `crypt` module to compare the original password with the stored hash using the `pwd_context.verify()` method
- Returns True if the password matches, False otherwise