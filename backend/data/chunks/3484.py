def test_path_float_True():
    response = client.get("/path/float/True")
    assert response.status_code == 422
    assert response.json() == IsDict(
        {
            "detail": [
                {
                    "type": "float_parsing",
                    "loc": ["path", "item_id"],
                    "msg": "Input should be a valid number, unable to parse string as a number",
                    "input": "True",
                    "url": match_pydantic_error_url("float_parsing"),
                }
            ]
        }
    ) | IsDict(
        # TODO: remove when deprecating Pydantic v1
        {
            "detail": [
                {
                    "loc": ["path", "item_id"],
                    "msg": "value is not a valid float",
                    "type": "type_error.float",
                }
            ]
        }
    )