- This function takes a `CurrentUser` object as input and returns the currently active superuser. - If the provided user is not a superuser, it raises an exception with a specific error message. - The returned value is always the same as the input `CurrentUser`, assuming that it represents a valid superuser.