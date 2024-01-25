def test_encode_dataclass():
    item = Item(name="foo", count=100)
    assert jsonable_encoder(item) == {"name": "foo", "count": 100}
    assert jsonable_encoder(item, include={"name"}) == {"name": "foo"}
    assert jsonable_encoder(item, exclude={"count"}) == {"name": "foo"}
    assert jsonable_encoder(item, include={}) == {}
    assert jsonable_encoder(item, exclude={}) == {"name": "foo", "count": 100}