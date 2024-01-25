@needs_py310
@pytest.mark.parametrize(
    "path,headers,expected_status,expected_response",
    [
        ("/items", None, 200, {"strange_header": None}),
        ("/items", {"X-Header": "notvalid"}, 200, {"strange_header": None}),
        (
            "/items",
            {"strange_header": "FastAPI test"},
            200,
            {"strange_header": "FastAPI test"},
        ),
        (
            "/items",
            {"strange-header": "Not really underscore"},
            200,
            {"strange_header": None},
        ),
    ],
)
def test(path, headers, expected_status, expected_response, client: TestClient):
    response = client.get(path, headers=headers)
    assert response.status_code == expected_status
    assert response.json() == expected_response