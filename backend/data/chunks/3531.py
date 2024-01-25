def test_path_param_le_int_42():
    response = client.get("/path/param-le-int/42")
    assert response.status_code == 422
    assert response.json() == IsDict(
        {
            "detail": [
                {
                    "type": "less_than_equal",
                    "loc": ["path", "item_id"],
                    "msg": "Input should be less than or equal to 3",
                    "input": "42",
                    "ctx": {"le": 3},
                    "url": match_pydantic_error_url("less_than_equal"),
                }
            ]
        }
    ) | IsDict(
        # TODO: remove when deprecating Pydantic v1
        {
            "detail": [
                {
                    "loc": ["path", "item_id"],
                    "msg": "ensure this value is less than or equal to 3",
                    "type": "value_error.number.not_le",
                    "ctx": {"limit_value": 3},
                }
            ]
        }
    )