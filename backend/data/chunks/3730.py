def test_nested_exclude_simple_dict():
    response = client.get("/simple_exclude_dict")
    assert response.status_code == 200, response.text
    assert response.json() == {
        "baz": "simple_exclude_dict model2 baz",
        "ref": {"foo": "simple_exclude_dict model foo"},
    }