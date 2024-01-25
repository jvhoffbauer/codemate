def test_post_validation_error():
    response = client.post("/items/", json={"title": "towel", "size": "XL"})
    assert response.status_code == 422, response.text
    assert response.json() == IsDict(
        {
            "detail": [
                {
                    "type": "int_parsing",
                    "loc": ["body", "size"],
                    "msg": "Input should be a valid integer, unable to parse string as an integer",
                    "input": "XL",
                    "url": match_pydantic_error_url("int_parsing"),
                }
            ],
            "body": {"title": "towel", "size": "XL"},
        }
    ) | IsDict(
        # TODO: remove when deprecating Pydantic v1
        {
            "detail": [
                {
                    "loc": ["body", "size"],
                    "msg": "value is not a valid integer",
                    "type": "type_error.integer",
                }
            ],
            "body": {"title": "towel", "size": "XL"},
        }
    )