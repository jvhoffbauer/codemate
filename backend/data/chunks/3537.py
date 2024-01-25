def test_path_param_ge_int_2():
    response = client.get("/path/param-ge-int/2")
    assert response.status_code == 422
    assert response.json() == IsDict(
        {
            "detail": [
                {
                    "type": "greater_than_equal",
                    "loc": ["path", "item_id"],
                    "msg": "Input should be greater than or equal to 3",
                    "input": "2",
                    "ctx": {"ge": 3},
                    "url": match_pydantic_error_url("greater_than_equal"),
                }
            ]
        }
    ) | IsDict(
        # TODO: remove when deprecating Pydantic v1
        {
            "detail": [
                {
                    "loc": ["path", "item_id"],
                    "msg": "ensure this value is greater than or equal to 3",
                    "type": "value_error.number.not_ge",
                    "ctx": {"limit_value": 3},
                }
            ]
        }
    )