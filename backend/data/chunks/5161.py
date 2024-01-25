def test_create_user():
    email = random_lower_string()
    password = random_lower_string()
    user_in = UserCreate(username=email, email=email, password=password)
    bucket = get_default_bucket()
    user = crud.user.upsert(bucket, user_in=user_in, persist_to=1)
    assert hasattr(user, "username")
    assert user.username == email
    assert hasattr(user, "hashed_password")
    assert hasattr(user, "type")
    assert user.type == "userprofile"