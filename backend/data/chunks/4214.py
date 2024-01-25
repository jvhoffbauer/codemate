def test_post_invalid_item():
    response = client.post("/items/", json={"name": "Foo", "price": "invalid price"})
    assert response.status_code == 422
    assert response.json() == IsDict(
        {
            "detail": [
                {
                    "type": "float_parsing",
                    "loc": ["body", "price"],
                    "msg": "Input should be a valid number, unable to parse string as a number",
                    "input": "invalid price",
                    "url": match_pydantic_error_url("float_parsing"),
                }
            ]
        }
    ) | IsDict(
        # TODO: remove when deprecating Pydantic v1
        {
            "detail": [
                {
                    "loc": ["body", "price"],
                    "msg": "value is not a valid float",
                    "type": "type_error.float",
                }
            ]
        }
    )