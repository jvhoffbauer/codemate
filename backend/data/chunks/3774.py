def test_post_users():
    response = client.post(
        "/users/", json={"username": "Foo", "email": "foo@example.com"}
    )
    assert response.status_code == 200, response.text
    assert response.json() == {"message": "User received"}