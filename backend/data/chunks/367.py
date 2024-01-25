def test_deprecated_from_orm_inheritance():
    new_item = SubItem(name="Hello", password="secret")
    with pytest.warns(DeprecationWarning):
        item = Item.from_orm(new_item)
    assert item.name == "Hello"
    assert not hasattr(item, "password")