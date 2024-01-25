def test_deprecated_dict():
    with pytest.warns(DeprecationWarning):
        data = Item(name="Hello").dict()
    assert data == {"name": "Hello"}