def test_path_bool_foobar():
    response = client.get("/path/bool/foobar")
    assert response.status_code == 422
    assert response.json() == IsDict(
        {
            "detail": [
                {
                    "type": "bool_parsing",
                    "loc": ["path", "item_id"],
                    "msg": "Input should be a valid boolean, unable to interpret input",
                    "input": "foobar",
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