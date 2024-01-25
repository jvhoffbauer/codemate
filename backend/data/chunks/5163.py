def test_not_authenticate_user():
    email = random_lower_string()
    password = random_lower_string()
    bucket = get_default_bucket()
    user = crud.user.authenticate(bucket, username=email, password=password)
    assert user is None