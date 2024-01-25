def test_get_route():
    response = client.get("/")
    assert response.status_code == 200, response.text
    assert response.json() == {}