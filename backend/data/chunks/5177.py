def test_retrieve_users(superuser_token_headers):
    server_api = get_server_api()
    username = random_lower_string()
    password = random_lower_string()
    user_in = UserCreate(username=username, email=username, password=password)
    bucket = get_default_bucket()
    user = crud.user.upsert(bucket, user_in=user_in, persist_to=1)

    username2 = random_lower_string()
    password2 = random_lower_string()
    user_in2 = UserCreate(username=username2, email=username2, password=password2)
    user2 = crud.user.upsert(bucket, user_in=user_in, persist_to=1)

    r = requests.get(
        f"{server_api}{config.API_V1_STR}/users/", headers=superuser_token_headers
    )
    all_users = r.json()

    assert len(all_users) > 1
    for user in all_users:
        assert "username" in user
        assert "admin_roles" in user