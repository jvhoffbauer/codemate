def test_get_timed():
    response = client.get("/timed")
    assert response.json() == {"message": "It's the time of my life"}
    assert "X-Response-Time" in response.headers
    assert float(response.headers["X-Response-Time"]) >= 0