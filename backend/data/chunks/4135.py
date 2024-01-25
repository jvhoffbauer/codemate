def test_get():
    response = client.get("/")
    assert response.json() == {"message": "Not timed"}
    assert "X-Response-Time" not in response.headers