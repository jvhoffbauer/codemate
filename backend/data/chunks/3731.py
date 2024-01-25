def test_nested_include_mixed():
    response = client.get("/mixed")
    assert response.status_code == 200, response.text
    assert response.json() == {
        "name": "mixed model3 name",
        "ref2": {
            "ref": {"foo": "mixed model foo", "bar": "mixed model bar"},
        },
    }