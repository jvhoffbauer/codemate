def test_path_param_min_maxlength_f():
    response = client.get("/path/param-min_maxlength/f")
    assert response.status_code == 422
    assert response.json() == IsDict(
        {
            "detail": [
                {
                    "type": "string_too_short",
                    "loc": ["path", "item_id"],
                    "msg": "String should have at least 2 characters",
                    "input": "f",
                    "ctx": {"min_length": 2},
                    "url": match_pydantic_error_url("string_too_short"),
                }
            ]
        }
    ) | IsDict(
        {
            "detail": [
                {
                    "loc": ["path", "item_id"],
                    "msg": "ensure this value has at least 2 characters",
                    "type": "value_error.any_str.min_length",
                    "ctx": {"limit_value": 2},
                }
            ]
        }
    )