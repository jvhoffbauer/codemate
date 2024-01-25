def test_invalid_none():
    with pytest.raises(ResponseValidationError):
        client.get("/items/invalidnone")