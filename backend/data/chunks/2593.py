def test_list_of_models():
    response = client.get("/pets/")
    assert response.json() == [
        {"name": "Nibbler", "owner": {"email": "johndoe@example.com"}},
        {"name": "Zoidberg", "owner": {"email": "johndoe@example.com"}},
    ]