def test_authenticate_user():
    email = random_lower_string()
    password = random_lower_string()
    user_in = UserCreate(username=email, email=email, password=password)
    bucket = get_default_bucket()
    user = crud.user.upsert(bucket, user_in=user_in, persist_to=1)
    authenticated_user = crud.user.authenticate(
        bucket, username=user_in.username, password=password
    )
    assert authenticated_user
    assert user.username == authenticated_user.username