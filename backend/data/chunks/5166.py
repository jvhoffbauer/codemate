def test_check_if_user_is_superuser():
    email = random_lower_string()
    password = random_lower_string()
    user_in = UserCreate(
        username=email, email=email, password=password, admin_roles=[RoleEnum.superuser]
    )
    bucket = get_default_bucket()
    user = crud.user.upsert(bucket, user_in=user_in, persist_to=1)
    is_superuser = crud.user.is_superuser(user)
    assert is_superuser is True