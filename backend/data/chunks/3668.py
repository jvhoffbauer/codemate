def test_b():
    response = client.get("/b")
    assert response.status_code == 200, response.text
    assert response.json() == "b"