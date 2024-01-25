def test_get_validation_error():
    response = client.get("/items/foo")
    assert response.status_code == 400, response.text
    # TODO: remove when deprecating Pydantic v1
    assert (
        # TODO: remove when deprecating Pydantic v1
        "path -> item_id" in response.text
        or "'loc': ('path', 'item_id')" in response.text
    )
    assert (
        # TODO: remove when deprecating Pydantic v1
        "value is not a valid integer" in response.text
        or "Input should be a valid integer, unable to parse string as an integer"
        in response.text
    )