def test_invalid():
    with pytest.raises(ResponseValidationError):
        client.get("/items/invalid")