def test_get_user():
    password = random_lower_string()
    username = random_lower_string()
    user_in = UserCreate(
        username=username,
        email=username,
        password=password,
        admin_roles=[RoleEnum.superuser],
    )
    bucket = get_default_bucket()
    user = crud.user.upsert(bucket=bucket, user_in=user_in, persist_to=1)
    user_2 = crud.user.get(bucket, username=username)
    assert user.username == user_2.username
    assert jsonable_encoder(user) == jsonable_encoder(user_2)