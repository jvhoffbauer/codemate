- Updates the currently logged in user's information using PUT request with optional parameters for password, full name, and email. - Retrieves the current user from the database using `Depends(get_current_active_user)`. - Creates a new instance of `UserUpdate` class with the current user's data as initial values. - If any of the optional parameters are provided, updates their corresponding fields in the `UserUpdate` object. - Uses the `crud.user.update()` function to save the updated user to the database. - Returns the updated user object.