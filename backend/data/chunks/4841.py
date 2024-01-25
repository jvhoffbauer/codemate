def test_token_inactive_user():
    access_token = get_access_token(
        username="alice", password="secretalice", scope="me"
    )
    response = client.get(
        "/users/me", headers={"Authorization": f"Bearer {access_token}"}
    )
    assert response.status_code == 400, response.text
    assert response.json() == {"detail": "Inactive user"}