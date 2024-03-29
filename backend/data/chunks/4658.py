def test_get_invalid_one_users():
    response = client.get("/users/", headers={"X-Token": "invalid"})
    assert response.status_code == 400, response.text
    assert response.json() == {"detail": "X-Token header invalid"}