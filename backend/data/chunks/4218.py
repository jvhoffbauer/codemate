def test_post_authors_item():
    response = client.post(
        "/authors/foo/items/",
        json=[{"name": "Bar"}, {"name": "Baz", "description": "Drop the Baz"}],
    )
    assert response.status_code == 200
    assert response.json() == {
        "name": "foo",
        "items": [
            {"name": "Bar", "description": None},
            {"name": "Baz", "description": "Drop the Baz"},
        ],
    }