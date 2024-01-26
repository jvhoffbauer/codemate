- This function authenticates a user using their email and password provided in `AuthUser`. - It retrieves the user from the database using `get_user_by_email`, raises an exception (`InvalidCredentials`) if the user is not found. - If the user exists, it checks whether the given password matches the stored one using `check_password`, raising another exception (also `InvalidCredentials`) if they don't match. - The successfully authenticated user is returned as a dictionary containing all its attributes.