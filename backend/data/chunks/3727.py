def test_nested_include_simple():
    response = client.get("/simple_include")

    assert response.status_code == 200, response.text

    assert response.json() == {
        "baz": "simple_include model2 baz",
        "ref": {"foo": "simple_include model foo"},
    }