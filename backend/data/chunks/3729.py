def test_nested_exclude_simple():
    response = client.get("/simple_exclude")
    assert response.status_code == 200, response.text
    assert response.json() == {
        "baz": "simple_exclude model2 baz",
        "ref": {"foo": "simple_exclude model foo"},
    }