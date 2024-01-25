def test_get():
    response = client.get("/items/")
    assert response.status_code == 200, response.text