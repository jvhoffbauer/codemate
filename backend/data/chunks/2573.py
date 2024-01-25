def test_double_invalid():
    with pytest.raises(ResponseValidationError):
        client.get("/items/innerinvalid")