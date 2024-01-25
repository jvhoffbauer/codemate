@needs_py310
def test_no_hidden_query(client: TestClient):
    response = client.get("/items")
    assert response.status_code == 200, response.text
    assert response.json() == {"hidden_query": "Not found"}