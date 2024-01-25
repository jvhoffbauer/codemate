def test_get():
    response = client.get("/")
    assert response.text == html