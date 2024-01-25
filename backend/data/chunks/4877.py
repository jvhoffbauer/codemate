def test_inactive_user():
    response = client.get("/users/me", headers={"Authorization": "Bearer alice"})
    assert response.status_code == 400, response.text
    assert response.json() == {"detail": "Inactive user"}