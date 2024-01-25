def test_create_user_existing_username(
    client: TestClient, superuser_token_headers: dict, db: Session
):
    username = random_email()  # username = email
    password = random_lower_string()
    user_in = UserCreate(email=username, password=password)
    crud.user.create(db, obj_in=user_in)
    data = {"email": username, "password": password}
    response = client.post(
        f"{settings.API_STR}{settings.API_V1_STR}/users",
        headers=superuser_token_headers,
        json=data,
    )
    created_user = response.json()
    assert response.status_code == 400
    assert "_id" not in created_user