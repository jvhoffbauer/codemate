def test_filter_top_level_model():
    response = client.post(
        "/users", json={"email": "johndoe@example.com", "password": "secret"}
    )
    assert response.json() == {"email": "johndoe@example.com"}