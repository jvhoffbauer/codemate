def test_invalid_list():
    with pytest.raises(ResponseValidationError):
        client.get("/items/invalidlist")