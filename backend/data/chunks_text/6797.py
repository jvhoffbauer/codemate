- This function takes a `current_user` parameter annotated with `Annotated[User, Depends(get_current_user)]`. - It checks whether the `current_user` is active using the `is_active` attribute of the `User` model. - If the `current_user` is inactive (i.e., its `is_active` attribute is false), it raises a `HTTPException` with status code 400 and error message "Inactive user". - Otherwise, it returns the `current_user` object as is.