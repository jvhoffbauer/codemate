- Creates a new user using `crud.create_user()` function from some library called `crud`.
- Checks for existing users with the same email address using `crud.get_user_by_email()`, raises an error if found.
- Sends a welcome email to the newly created user's email address (if emails are enabled). The email is sent by calling `send_new_account_email()` function passing the user's email, username, and password as arguments.