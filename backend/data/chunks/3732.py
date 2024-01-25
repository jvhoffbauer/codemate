def test_nested_include_mixed_dict():
    response = client.get("/mixed_dict")
    assert response.status_code == 200, response.text
    assert response.json() == {
        "name": "mixed_dict model3 name",
        "ref2": {
            "ref": {"foo": "mixed_dict model foo", "bar": "mixed_dict model bar"},
        },
    }