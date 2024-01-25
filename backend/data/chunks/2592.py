def test_filter_second_level_model():
    response = client.get("/pets/1")
    assert response.json() == {
        "name": "Nibbler",
        "owner": {"email": "johndoe@example.com"},
    }