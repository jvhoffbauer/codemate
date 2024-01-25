def test_d():
    response = client.get("/d")
    assert response.status_code == 200, response.text
    assert response.json() == "d"