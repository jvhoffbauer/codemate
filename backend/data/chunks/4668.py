@needs_py39
@pytest.mark.parametrize(
    "path,expected_status,expected_response",
    [
        (
            "/items",
            200,
            {
                "items": [
                    {"item_name": "Foo"},
                    {"item_name": "Bar"},
                    {"item_name": "Baz"},
                ]
            },
        ),
        (
            "/items?q=foo",
            200,
            {
                "items": [
                    {"item_name": "Foo"},
                    {"item_name": "Bar"},
                    {"item_name": "Baz"},
                ],
                "q": "foo",
            },
        ),
        (
            "/items?q=foo&skip=1",
            200,
            {"items": [{"item_name": "Bar"}, {"item_name": "Baz"}], "q": "foo"},
        ),
        (
            "/items?q=bar&limit=2",
            200,
            {"items": [{"item_name": "Foo"}, {"item_name": "Bar"}], "q": "bar"},
        ),
        (
            "/items?q=bar&skip=1&limit=1",
            200,
            {"items": [{"item_name": "Bar"}], "q": "bar"},
        ),
        (
            "/items?limit=1&q=bar&skip=1",
            200,
            {"items": [{"item_name": "Bar"}], "q": "bar"},
        ),
    ],
)
def test_get(path, expected_status, expected_response, client: TestClient):
    response = client.get(path)
    assert response.status_code == expected_status
    assert response.json() == expected_response