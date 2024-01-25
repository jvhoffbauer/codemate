def test_path_bool_42():
    response = client.get("/path/bool/42")
    assert response.status_code == 422
    assert response.json() == IsDict(
        {
            "detail": [
                {
                    "type": "bool_parsing",
                    "loc": ["path", "item_id"],
                    "msg": "Input should be a valid boolean, unable to interpret input",
                    "input": "42",
                    "url": match_pydantic_error_url("bool_parsing"),
                }
            ]
        }
    ) | IsDict(
        # TODO: remove when deprecating Pydantic v1
        {
            "detail": [
                {
                    "loc": ["path", "item_id"],
                    "msg": "value could not be parsed to a boolean",
                    "type": "type_error.bool",
                }
            ]
        }
    )