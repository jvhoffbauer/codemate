@needs_py39
@pytest.mark.parametrize(
    "path,expected_status,expected_response",
    [
        ("/items", 200, {"q": None, "skip": 0, "limit": 100}),
        ("/items?q=foo", 200, {"q": "foo", "skip": 0, "limit": 100}),
        ("/items?q=foo&skip=5", 200, {"q": "foo", "skip": 5, "limit": 100}),
        ("/items?q=foo&skip=5&limit=30", 200, {"q": "foo", "skip": 5, "limit": 30}),
        ("/users", 200, {"q": None, "skip": 0, "limit": 100}),
    ],
)
def test_get(path, expected_status, expected_response, client: TestClient):
    response = client.get(path)
    assert response.status_code == expected_status
    assert response.json() == expected_response