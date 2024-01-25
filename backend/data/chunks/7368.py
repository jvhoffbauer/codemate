def test_create_user_new_email(client: TestClient, db: Session):
    email = random_email()
    password = random_lower_string()
    data = {
        "email": email,
        "password": password,
        "is_superuser": True,
        "is_active": False,
    }
    response = client.post(
        f"{settings.API_STR}{settings.API_V1_STR}/users/open",
        json=data,
    )
    assert 200 <= response.status_code < 300

    user = crud.user.get_by_email(db, email=email)
    assert user
    assert user.email == email
    assert user.is_superuser is False
    assert user.is_active