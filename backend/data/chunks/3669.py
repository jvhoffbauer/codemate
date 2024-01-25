def test_c():
    response = client.get("/c")
    assert response.status_code == 200, response.text
    assert response.json() == "c"