@needs_py39
def test_get(client: TestClient, html: str):
    response = client.get("/")
    assert response.text == html