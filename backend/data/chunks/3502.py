def test_path_param_min_maxlength_foobar():
    response = client.get("/path/param-min_maxlength/foobar")
    assert response.status_code == 422
    assert response.json() == IsDict(
        {
            "detail": [
                {
                    "type": "string_too_long",
                    "loc": ["path", "item_id"],
                    "msg": "String should have at most 3 characters",
                    "input": "foobar",
                    "ctx": {"max_length": 3},
                    "url": match_pydantic_error_url("string_too_long"),
                }
            ]
        }
    ) | IsDict(
        # TODO: remove when deprecating Pydantic v1
        {
            "detail": [
                {
                    "loc": ["path", "item_id"],
                    "msg": "ensure this value has at most 3 characters",
                    "type": "value_error.any_str.max_length",
                    "ctx": {"limit_value": 3},
                }
            ]
        }
    )