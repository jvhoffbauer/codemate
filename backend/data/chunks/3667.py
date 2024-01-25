def test_a():
    response = client.get("/a")
    assert response.status_code == 200, response.text
    assert response.json() == "a"