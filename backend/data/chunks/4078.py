@needs_py39
def test_multi_query_values(client: TestClient):
    url = "/items/?q=baz&q=foobar"
    response = client.get(url)
    assert response.status_code == 200, response.text
    assert response.json() == {"q": ["baz", "foobar"]}