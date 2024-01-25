def test_nested_include_simple_dict():
    response = client.get("/simple_include_dict")

    assert response.status_code == 200, response.text

    assert response.json() == {
        "baz": "simple_include_dict model2 baz",
        "ref": {"foo": "simple_include_dict model foo"},
    }