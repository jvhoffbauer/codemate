def test_get_items():
    response = client.get("/items/")
    assert response.status_code == 200, response.text
    assert response.json() == ["Portal gun", "Plumbus"]