def test_request_class():
    response = client.get("/check-class")
    assert response.json() == {"request_class": "GzipRequest"}