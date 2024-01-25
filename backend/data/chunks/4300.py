@needs_py310
@pytest.mark.parametrize(
    "path,headers,expected_status,expected_response",
    [
        ("/items", None, 200, {"User-Agent": "testclient"}),
        ("/items", {"X-Header": "notvalid"}, 200, {"User-Agent": "testclient"}),
        ("/items", {"User-Agent": "FastAPI test"}, 200, {"User-Agent": "FastAPI test"}),
    ],
)
def test(path, headers, expected_status, expected_response, client: TestClient):
    response = client.get(path, headers=headers)
    assert response.status_code == expected_status
    assert response.json() == expected_response