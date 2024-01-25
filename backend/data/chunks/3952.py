@pytest.mark.parametrize(
    "url,data",
    [
        ("/items/foo", {"name": "Foo", "price": 50.2}),
        (
            "/items/bar",
            {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
        ),
        (
            "/items/baz",
            {
                "name": "Baz",
                "description": None,
                "price": 50.2,
                "tax": 10.5,
                "tags": [],
            },
        ),
    ],
)
def test_get(url, data):
    response = client.get(url)
    assert response.status_code == 200, response.text
    assert response.json() == data