def authentication_token_from_email(email):
    """
    Return a valid token for the user with given email.

    If the user doesn't exist it is created first.
    """
    password = random_lower_string()
    bucket = get_default_bucket()

    user = crud.user.get_by_email(bucket, email=email)
    if not user:
        user_in = UserCreate(username=email, email=email, password=password)
        user = crud.user.upsert(bucket, user_in=user_in, persist_to=1)
    else:
        user_in = UserUpdate(password=password)
        user = crud.user.update(bucket, user=user, user_in=user_in)

    return user_authentication_headers(get_server_api(), email, password)