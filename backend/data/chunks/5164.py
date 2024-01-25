def test_check_if_user_is_active():
    email = random_lower_string()
    password = random_lower_string()
    user_in = UserCreate(username=email, email=email, password=password)
    bucket = get_default_bucket()
    user = crud.user.upsert(bucket, user_in=user_in, persist_to=1)
    is_active = crud.user.is_active(user)
    assert is_active is True