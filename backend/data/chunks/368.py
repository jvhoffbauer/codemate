def test_deprecated_parse_obj():
    with pytest.warns(DeprecationWarning):
        item = Item.parse_obj({"name": "Hello"})
    assert item.name == "Hello"