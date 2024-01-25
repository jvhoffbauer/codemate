def test_path_param_minlength_fo():
    response = client.get("/path/param-minlength/fo")
    assert response.status_code == 422
    assert response.json() == IsDict(
        {
            "detail": [
                {
                    "type": "string_too_short",
                    "loc": ["path", "item_id"],
                    "msg": "String should have at least 3 characters",
                    "input": "fo",
                    "ctx": {"min_length": 3},
                    "url": match_pydantic_error_url("string_too_short"),
                }
            ]
        }
    ) | IsDict(
        # TODO: remove when deprecating Pydantic v1
        {
            "detail": [
                {
                    "loc": ["path", "item_id"],
                    "msg": "ensure this value has at least 3 characters",
                    "type": "value_error.any_str.min_length",
                    "ctx": {"limit_value": 3},
                }
            ]
        }
    )