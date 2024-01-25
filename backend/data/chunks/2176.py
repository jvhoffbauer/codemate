def test_get_invalid():
    response = client.get("/foo")
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY